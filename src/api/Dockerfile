FROM alpine:3.6
MAINTAINER Leland Later '<llater@ataraxia.io>'

EXPOSE 10101
WORKDIR /usr/src/app

RUN apk add --no-cache \
    uwsgi \
    uwsgi-python3 \
    python3

COPY . .
RUN rm -rf public/*

RUN pip3 install --no-cachr-dir -r requirements.txt
CMD [ "uwsgi", "--socket", "0.0.0.0:9000", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "manage:gui" ]