FROM phusion/baseimage:0.9.22
MAINTAINER LelandLater '<llater@ataraxia.io>'

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y &&
    apt-get install -y python2.7-minimal && \
                       python-pip

RUN mkdir -p /etc/my_init.d
COPY start_cue-api.sh /etc/my_init.d/start_cue-api.sh
RUN chmod +x /etc/my_init.d/start_cue-api.sh

COPY cue-api.service /etc/systemd/system/cue-api.service
RUN rm -f /etc/my_init.d/00_regen_ssh_host_keys.sh 
EXPOSE 10101
CMD ["/sbin/my_init"]
