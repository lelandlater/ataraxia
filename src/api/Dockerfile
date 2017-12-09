FROM alpine:3.6
MAINTAINER Leland Later '<llater@ataraxia.io>'

EXPOSE 10101
WORKDIR /usr/src/app

RUN apk add --no-cache \
    uwsgi \
    uwsgi-python3 \
    python3

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python3", "manage.py" ]
#CMD [ "uwsgi", "--emperor", "/usr/src/app" ]