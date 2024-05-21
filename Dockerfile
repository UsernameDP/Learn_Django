# use ubuntu as base image
FROM ubuntu:20.04
WORKDIR /app

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev libpq-dev 
RUN apt-get clean

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app/ 

EXPOSE 8000