FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /home/code
RUN pip install --upgrade pip
COPY ./requirements.txt /home/code/requirements.txt
RUN pip install -r requirements.txt

COPY . /home/code