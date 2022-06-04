FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-chache-dir --upgrade -r requirements.txt