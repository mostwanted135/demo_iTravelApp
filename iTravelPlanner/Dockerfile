FROM python:3.6.1-alpine
MAINTAINER WydahTeam

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
 && pip install cython \
 && apk del .build-deps

RUN pip install -r /app/requirements.txt
COPY . /app

EXPOSE 8000
CMD python /app/manage.py runserver 0.0.0.0:8000


