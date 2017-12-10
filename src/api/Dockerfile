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
#ENTRYPOINT [ "/bin/sh", "-c", "echo", "'This is up!'" ]
CMD [ "python3", "-i", "manage.py" ]
#CMD [ "uwsgi", "--emperor", "/usr/src/app" ]
