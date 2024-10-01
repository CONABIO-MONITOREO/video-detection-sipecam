FROM python:3.11

WORKDIR /app

COPY ./main.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt