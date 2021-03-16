FROM python:3-alpine

MAINTAINER Peter Fisher

COPY ./apps/requirements.txt /apps/requirements.txt

WORKDIR /savanaApiFinal
#${WORKSPACE}/Dockerfile

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./apps /app

CMD python app.py run -h 0.0.0.0