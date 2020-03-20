FROM python:3.8-alpine as build-container

LABEL MAINTAINER="XCNT GmbH <dev-infra@xcnt.io>"

WORKDIR /pip-packages

ADD requirements.txt /pip-packages

RUN apk add --update postgresql-dev pcre-dev gcc musl-dev python3-dev linux-headers libffi-dev
RUN pip download --no-cache-dir -r requirements.txt

ADD . /opt/app

FROM python:3.8-alpine

LABEL MAINTAINER="XCNT GmbH <dev-infra@xcnt.io>"

WORKDIR /opt/app

COPY --from=build-container /pip-packages /pip-packages

RUN apk add --update postgresql-dev pcre-dev

RUN ln /pip-packages/requirements.txt /opt/app/requirements.txt && \
    apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev linux-headers libffi-dev && \
    pip install --no-cache-dir --find-links=/pip-packages/ -r requirements.txt && \
    pip install https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi && \
    apk del .build-deps

COPY --from=build-container /opt/app /opt/app

USER 9000
EXPOSE 8080

CMD [ "uwsgi", "--http", "0.0.0.0:8080", \
               "--wsgi-file", "run.py", \
               "--uid", "9000", \
               "--processes", "1", \
               "--threads", "16", \
               "--callable", "application" ]