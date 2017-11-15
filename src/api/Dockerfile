FROM phusion/baseimage:0.9.22
MAINTAINER LelandLater '<llater@ataraxia.io>'

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && \
    apt-get install -y python2.7 \
                       python-pip \
                       build-essential \
                       python-dev \
                       libpcre3 \
                       libpcre3-dev \
                       libssl-dev
RUN mkdir -p /etc/my_init.d/
COPY start_cueapi.sh /etc/my_init.d/start_cueapi.sh
RUN chmod +x /etc/my_init.d/start_cueapi.sh

RUN mkdir /cueapi
ADD requirements.txt /cueapi/requirements.txt
RUN pip install -r /cueapi/requirements.txt
COPY . /cueapi

RUN rm -f /etc/my_init.d/00_regen_ssh_host_keys.sh

EXPOSE 10101

CMD ["/sbin/my_init"]
