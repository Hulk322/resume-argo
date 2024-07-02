FROM python:3.8.5-slim 
WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev build-essential gcc 
#libpoppler-cpp-dev pkg-config libicu-dev libxml2 libxslt1-dev libatlas-base-dev liblapack-dev libblas-dev gfortran

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

ENV PATH=/root/.local/bin:$PATH

COPY nlptest.py ./

RUN python nlptest.py

COPY . .

EXPOSE 9028

CMD ["python3","-u","main.py"]


