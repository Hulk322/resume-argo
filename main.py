##@Job vs Resume Matcher API
#This module is used to Launch a Rest API for Matching jobs and resumes.

# SYSTEM IMPORT CLASS
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
import uvicorn
import re
import time
from starlette.responses import JSONResponse
from starlette import status
import threading
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor
import asyncio
import logging

# USER IMPORT CLASS
from logger import standardLogger
import config


from resume_normalization_client import ResumeNorm


api_logger = standardLogger().get_logger("Resume Norm API Logger")
app = FastAPI(title='Resume Norm API')
# to get a string like this run:
# openssl rand -hex 32
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
FLOAT_NUMBER_PATTERN = re.compile("^(\d+(\.\d+){0,1})$")

# add cors link
origins = ["http://localhost:2000",
           "http://localhost:4200",
           "http://localhost:8080", "https://dev.simplify-ai.com", "https://qa.simplify-ai.com"]

count = 0
overall_count = 0
rejected_count = 0
QUEUE_THRESHOLD = multiprocessing.cpu_count()
lock = threading.Lock()
SET_LIMIT = True


def increase():
    global count
    global overall_count
    global rejected_count
    valid_thread = False
    lock.acquire()
    try:
        if count < QUEUE_THRESHOLD:
            count += 1
            overall_count += 1
            valid_thread = True
        else:
            rejected_count += 1
    finally:
        lock.release()
        return valid_thread


def decrease():
    global count
    lock.acquire()
    try:
        count -= 1
    finally:
        lock.release()


def getCount():
    global count
    return count


def getOverallCount():
    global overall_count
    return overall_count


def getRejectedCount():
    global rejected_count

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def errorhandler(code, msg):
    ErrorDict = {}
    ErrorDict["Code"] = code
    ErrorDict["Message"] = msg
    return ErrorDict


class Token(BaseModel):
    access_token: str
    token_type: str


class Job(BaseModel):
    matchingType: str
    job: Optional[dict] = None
    resume: Optional[dict] = None
    job2: Optional[dict] = None
    resume2: Optional[dict] = None


class ParseResume(BaseModel):
    parse_response: dict

@app.on_event("startup")
async def startup_event():
    print("We are in start-up function...")
    cpus = multiprocessing.cpu_count()
    if cpus > 1:
        cpus -= 1
    app.executor = ProcessPoolExecutor(max_workers=cpus)
    app.loop = asyncio.get_event_loop()
    app.resume_norm = ResumeNorm()

@app.on_event("shutdown")
async def shutdown_event():
    print("We are in shut-down function...")
    app.executor.shutdown()

async def run_in_process(fn, *args):
    return await app.loop.run_in_executor(
        app.executor, fn, *args)  # wait and return result

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta and not FLOAT_NUMBER_PATTERN.sub("", expires_delta):
        expire = datetime.utcnow() + timedelta(minutes=float(expires_delta))
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), access_token_expires=None):
    api_logger.info("form data: {}".format(form_data))
    user = form_data.username == config.USER and form_data.password == config.PASSWORD
    if not user:
        return errorhandler(config.ERROR_CODE_401,
                            config.ERROR_MSG_UNAME_AND_PASS_NOT_MATHCED)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}



@app.get('/', include_in_schema=False)
async def check_server():
    """ help to check server is live or not """
    response = {"info": "Resume Norm API is started"}
    #return HTMLResponse(status_code=200, content=result)
    return response


@app.post('/resume/normalization')
async def resume_normalization(parse_resume: ParseResume) -> JSONResponse:
    """
    Routes to call Resume Normalization
    :param request: for logging
    :param data: document_as_base_64_string
    :return: JSON output
    """
    response = {}
    if SET_LIMIT:
        global count
        if count < QUEUE_THRESHOLD and increase():
            try:
                logging.warning("=====> Counter: {}, threshold: {}".format(count, QUEUE_THRESHOLD))
                # resume_norm = ResumeNorm()
                result = await run_in_process(
                                            app.resume_norm.normalize_resume, parse_resume.parse_response)
                # return JSONResponse(resume_norm.normalize_resume(parse_resume.parse_response))
                return JSONResponse(result)
            
            except Exception as e:
                api_logger.error('Error: {}'.format(e))
                response.update(
                    errorhandler(status.HTTP_500_INTERNAL_SERVER_ERROR, config.ERROR_MSG_SERVER_ERROR))
            finally:
                decrease()
    return response


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=9028,
        host="0.0.0.0""TZ-ALB-637020186.ap-south-1.elb.amazonaws.com",
    )
