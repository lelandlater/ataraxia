FROM phusion/baseimage:0.9.22
MAINTAINER LelandLater '<llater@ataraxia.io>'

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && \
    apt-get install -y python2.7 python-pip build-essential python-dev libpcre3 libpcre3-dev

RUN mkdir -p /etc/my_init.d
ADD start_cuegui.sh /etc/my_init.d/start_cuegui.sh
RUN chmod +x /etc/my_init.d/start_cuegui.sh

RUN mkdir /cuegui
ADD requirements.txt /cuegui/requirements.txt
RUN pip install uwsgi
RUN pip install -r /cuegui/requirements.txt
 
COPY . /cuegui

RUN rm -f /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]
