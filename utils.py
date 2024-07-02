'''
Created on 09-Mar-2021

@author: rohitk
'''

import requests
import json
import time
import asyncio
import aiohttp
import config
from logger import standardLogger

util_logger = standardLogger().get_logger("Utility Logger")


def normalize_job_titles(titles):
    r = None
    try:
        util_logger.info("====>API call")
        r = requests.post(
            config.TITLE_NORM_API_URL,
            headers={
                "Authorization": "Bearer " + config.TITLE_NORM_API_ACCESS_TOKEN
            },
            json={
                config.TITLE_NORM_API_JOBS_FIELD: [{
                    config.TITLE_NORM_API_TITLE_FIELD:
                    title
                } for title in titles]
            }).json()
        r = r[config.TITLE_NORM_API_RESPONSE_FIELD]
    except Exception as e:
        util_logger.error(
            "Error in normalization: {}, titles:{}, r: {}".format(
                e, titles, r))
        r = None
    for i, title in enumerate(titles):
        if not r or len(r) <= i:
            r.append({
                config.PARSED_MAIN_JOB_TITLE_FIELD: title,
                config.TITLE_NORM_API_RESPONSE_SCORE_FIELD: None
            })
        elif not r[i].get(config.TITLE_NORM_API_RESPONSE_NORM_TITLE_FIELD):
            r[i] = {
                config.PARSED_MAIN_JOB_TITLE_FIELD: title,
                config.TITLE_NORM_API_RESPONSE_SCORE_FIELD: None
            }
        else:
            r[i][config.PARSED_MAIN_JOB_TITLE_FIELD] = r[i][
                config.TITLE_NORM_API_RESPONSE_NORM_TITLE_FIELD]
    return r


def normalize_resume_titles(titles):
    r = None
    try:

        util_logger.info("====>API call")
        r = requests.post(
            config.TITLE_NORM_API_URL,
            headers={
                "Authorization": "Bearer " + config.TITLE_NORM_API_ACCESS_TOKEN
            },
            json={
                config.TITLE_NORM_API_JOBS_FIELD: [{
                    config.TITLE_NORM_API_TITLE_FIELD:
                    title
                } for title in titles]
            }).json()

        r = r[config.TITLE_NORM_API_RESPONSE_FIELD]
    except Exception as e:
        util_logger.error(
            "Error in normalize_resume_titles normalization: {}, titles:{}, r: {}".
            format(e, titles, r))
        r = None
    for i, title in enumerate(titles):
        if not r or len(r) <= i:
            r.append({
                config.PARSED_MAIN_JOB_TITLE_FIELD: title,
                config.TITLE_NORM_API_RESPONSE_SCORE_FIELD: None
            })
        elif not r[i].get(config.TITLE_NORM_API_RESPONSE_NORM_TITLE_FIELD):
            r[i] = {
                config.PARSED_MAIN_JOB_TITLE_FIELD: title,
                config.TITLE_NORM_API_RESPONSE_SCORE_FIELD: None
            }
        else:
            r[i][config.PARSED_MAIN_JOB_TITLE_FIELD] = r[i][
                config.TITLE_NORM_API_RESPONSE_NORM_TITLE_FIELD]
    return r


def create_edu_object(major=None,
                      degree=None,
                      course=None,
                      school=None,
                      university=None,
                      location=None,
                      city=None,
                      state=None,
                      country=None,
                      school_type=None):
    return [
        {
        config.EDUCATION_NORM_API_MAJOR_FIELD: major,
        config.EDUCATION_NORM_API_DEGREE_FIELD: degree,
        config.EDUCATION_NORM_API_SCHOOL_FIELD: school
        },
        {
        config.EDUCATION_NORM_API_COURSE_FIELD: course,
        config.EDUCATION_NORM_API_UNIVERSITY_FIELD: university,
        config.EDUCATION_NORM_API_CITY_FIELD: city,
        config.EDUCATION_NORM_API_STATE_FIELD: state,
        config.EDUCATION_NORM_API_COUNTRY_FIELD: country,
        config.EDUCATION_NORM_API_LOCATION_FIELD: location,
        config.EDUCATION_NORM_API_SCHOOL_TYPE_FIELD: school_type
        }
    ]



def normalize_education_data(edu_data_list):
    r = None
    request_data = {
        config.EDUCATION_NORM_API_EDUCATION_FIELD: edu_data_list
    }
    util_logger.info("Request data for normalize_education_data %s" % json.dumps(request_data))
    try:
        util_logger.info("====>API call")
        r = requests.post(
            config.EDUCATION_NORM_API_URL,
            headers={
                "Authorization":
                "Bearer " + config.EDUCATION_NORM_API_ACCESS_TOKEN
            },
            json=request_data).json().get("normalizedEducations",[])
            #json=json.dumps(request_data)).json()[
            #    config.EDUCATION_NORM_API_RESPONSE_NORMALIZED_EDUCATIONS_FIELD]
    except Exception as e:
        util_logger.error(
            "Error in education normalization: {}, request:{}, r: {}".format(
                e, request_data, r))
    return r


def normalize_location(location=None, city=None, state=None, country=None):
    r = None

    if not location:
        location = filter(lambda k: k != None, [city, state, country])
        location = " - ".join(location) if location else ""

    request_data = {config.LOCATION_API_LOCATION_FIELD: location}
    util_logger.info("request data for location :{}".format(request_data))
    try:
        util_logger.info("====>API call")
        r = requests.post(
            config.LOCATION_API_URL,
            headers={
                "Authorization": "Bearer " + config.LOCATION_API_ACCESS_TOKEN
            },
            json=request_data).json()[config.LOCATION_API_RESPONSE_FIELD]
    except Exception as e:
        util_logger.error(
            "Error in normalize_location normalization: {}, request:{}, r: {}".
            format(e, request_data, r))
    return r

async def job_type_async(data):
    data_list = []
    try:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for desc in data:
                if desc:
                    task = asyncio.ensure_future(
                        normalize_job_types(
                            session, desc[0],desc[1],desc[2],desc[3]))
                    tasks.append(task)
            if tasks:
                data_list = await asyncio.gather(*tasks)
        return data_list
    except Exception as e:
        util_logger.error("Error in normalize_job_types normalization: {}".format(e))


async def normalize_job_types(session,title=None,
                        experience_texts=[],
                        soc_code=None,
                        job_type=""):
    r = None
    request_data = {
        config.JOB_TYPE_API_TITLE_FIELD: title,
        config.JOB_TYPE_API_EXPERIENCES_FIELD: experience_texts,
        config.JOB_TYPE_API_SOC_FIELD: soc_code,
        config.JOB_TYPE_API_JOB_TYPE_FIELD: job_type
    }
    #util_logger.info("Request data for Job Type %s" % request_data)
    try:
        util_logger.info("====>API call")
        while True:
            async with session.post(
                config.JOB_TYPE_API_URL,
                headers={
                    "Authorization": "Bearer " + config.JOB_TYPE_API_ACCESS_TOKEN
                },
                json=request_data) as response:
                r = await response.json()
            if r["Code"] == 429:
                pass
            else:
                break
    except Exception as e:
        util_logger.error(
            "Error in normalize_job_types normalization: {}, request:{}, r: {}".format(
                e, request_data, r))
    return r


def normalize_industry(jobs=[]):
    r = None
    request_data = {config.INDUSTRY_CLF_API_REQUEST_JOBS_FIELD: jobs}
    #util_logger.info("Request for Normalize Industry %s" % request_data)
    try:
        util_logger.info("====>API call")
        r = requests.post(
            config.INDUSTRY_CLF_API_URL + config.INDUSTRY_CLF_API_CLF_CONTEXT,
            headers={
                "Authorization":
                "Bearer " + config.INDUSTRY_CLF_API_ACCESS_TOKEN
            },
            json=request_data).json()[
                config.INDUSTRY_CLF_API_RESPONSE_INDUSTRIES_FIELD]
    except Exception as e:
        util_logger.error(
            "Error in industry normalization: {}, request:{}, r: {}".format(
                e, request_data, r))
    return r if r else []


def normalize_skills(skills):
    r = []
    try:

        #util_logger.info("calling URL %s " % config.RESUME_SKILLS_NORM_API_URL)
        #util_logger.info("PAYLOAD is %s " % {config.SKILLS_NORM_API_REQUEST_SKILLS_FIELD: skills})

        util_logger.info("====>API call")
        r = requests.post(
            config.RESUME_SKILLS_NORM_API_URL,
            json={
                config.SKILLS_NORM_API_REQUEST_SKILLS_FIELD: skills
            }).json()

        #util_logger.info("Response from API is %s " % r)
        r = r.get('success').get('data')
    except Exception as e:
        util_logger.error(
            "Error in normalization: {}, skills:{}, r: {}".format(
                e, skills, r))
        r = []

    return r


def pick_industries_lies_in_k_percent_of_max(industries, k=20):
    max_limit = 1
    if len(industries) > 1:
        industries = sorted(
            industries,
            key=lambda k: k[config.INDUSTRY_CLF_API_CONFIDENCE_FIELD],
            reverse=True)
        max_conf = industries[0][config.INDUSTRY_CLF_API_CONFIDENCE_FIELD]
        for industry in industries[1:]:
            if float(industry[config.INDUSTRY_CLF_API_CONFIDENCE_FIELD]
                     ) / max_conf < (1.0 - float(k) / 100):
                break
            max_limit += 1
    return industries[:max_limit]


def merge_industry(workx_industry_list, workx_durations):
    result = []
    ''' NORM_INDUSTRY_FIELD - industryNormData
    INDUSTRY_CLF_API_RESPONSE_SOC_FIELD - socCode
    INDUSTRY_CLF_API_CONFIDENCE_FIELD - predictionConfidence
    '''
    SOC_FLD = config.INDUSTRY_CLF_API_RESPONSE_SOC_FIELD
    PRED_CONF_FLD = config.INDUSTRY_CLF_API_CONFIDENCE_FIELD

    workx_industry_list = list(
        map(lambda x: pick_industries_lies_in_k_percent_of_max(x),
            workx_industry_list))

    merged_soc = {}
    next_experience = 0
    for i, industry_list in enumerate(workx_industry_list):
        recency_weight = 0
        for k, w in config.RECENCY_RANGE_FOR_WORKX_PRIORITY.items():
            if next_experience >= k[0] and next_experience < k[1]:
                recency_weight = w
                break
        working_years = float(workx_durations[i]["durationInYears"])
        for item in industry_list:
            if item[SOC_FLD] in merged_soc:
                merged_soc[item[SOC_FLD]]['cnt'] += 1
                merged_soc[item[SOC_FLD]]['working_years'] += working_years
                merged_soc[item[SOC_FLD]]['pred_conf'] += item[
                    PRED_CONF_FLD] * recency_weight
            else:
                merged_soc[item[SOC_FLD]] = {
                    'item': item,
                    'cnt': 1,
                    'working_years': working_years,
                    'pred_conf': item[PRED_CONF_FLD] * recency_weight
                }
        next_experience += workx_durations[i]["durationInYears"]

    #print('merged_soc', merged_soc)
    for key in merged_soc:
        item = merged_soc[key]['item']
        #print('*****item', item)
        item[PRED_CONF_FLD] = float(
            merged_soc[key]['pred_conf']) / merged_soc[key]['cnt']
        item['working_years'] = merged_soc[key]['working_years']
        result.append(item)

    return pick_industries_lies_in_k_percent_of_max(result)


def categorise_skills(skills, result: dict, key: str):
    r = None
    request_data = {config.INDUSTRY_CLF_API_SKILLS_FIELD: skills}
    st = time.time()
    try:
        util_logger.info("====>API call")
        r = requests.post(
            config.INDUSTRY_CLF_API_URL +
            config.INDUSTRY_CLF_API_CATEGORIZATION_CONTEXT,
            headers={
                "Authorization":
                "Bearer " + config.INDUSTRY_CLF_API_ACCESS_TOKEN
            },
            json=request_data).json()[
                config.INDUSTRY_CLF_API_INDUSTRY_WISE_SKILLS_FIELD]
    except Exception as e:
        util_logger.error(
            "Error in industry normalization: {}, request:{}, r: {}".format(
                e, request_data, r))
    result[key] = r if r else []
    result['temp']['skills - categorization'] = time.time() - st
    return r if r else []
