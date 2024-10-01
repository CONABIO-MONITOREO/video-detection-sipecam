FROM python:3.11

WORKDIR /app

COPY ./main.py .
COPY ./requirements.txt .
COPY .env .

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

RUN pip install -r requirements.txt