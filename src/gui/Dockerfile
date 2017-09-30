
FROM phusion/baseimage:0.9.22
MAINTAINER LelandLater '<llater@ataraxia.io>'

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && \
    apt-get install -y python2.7 python-pip build-essential python-dev

RUN mkdir /cue-gui
ADD requirements.txt /cue-gui/requirements.txt
RUN pip install uwsgi
RUN pip install -r /cue-gui/requirements.txt

RUN mkdir -p /etc/my_init.d
ADD start_cue-gui.sh /etc/my_init.d/start_cue-gui.sh
RUN chmod +x /etc/my_init.d/start_cue-gui.sh
 
ADD cue-gui.service /etc/systemd/system/cue-gui.service
RUN rm -f /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]
