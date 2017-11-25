FROM alpine:latest
MAINTAINER Leland Later '<llater@ataraxia.io>'

EXPOSE 9000
WORKDIR /usr/src/app

RUN apk add --no-cache \
    uwsgi \
    uwsgi-python3 \
    python3

COPY . .

#RUN pip3 install --no-cache-dir -r requirements.txt
#CMD [ "wsgi", "--ini", "uwsgi.ini" ]
