FROM phusion/baseimage:0.9.22
MAINTAINER Leland Later '<llater@802secure.com>'

# add cue-api dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y -o APT::Install-Suggests=false \
      python-pip \
      python-dev \
      gcc \
      libmpfr-dev \
      libssl-dev \
      # IDK if all of these are essential 
      libmpc-dev \
      libffi-dev \
      build-essential \
      libpython-dev \
      python2.7-minimal \
      git \
      python-virtualenv \
      python-setuptools

# add start-up scripts
RUN mkdir -p /etc/my_init.d
COPY scripts/ /etc/my_init.d/
RUN chmod +x /etc/my_init.d/*.sh

## removes SSH key generation script
RUN rm -f /etc/my_init.d/00_regen_ssh_host_keys.sh


RUN pip install -r requirements.txt

# and copy config
RUN rm -rf /cowrie/cowrie-git/etc/cowrie.cfg
COPY cowrie.cfg /cowrie/cowrie-git/etc/

# allow cowrie user access
RUN chown -R cowrie /cowrie/cowrie-git/var && \
    chown -R cowrie /cowrie/cowrie-git/log && \
    chown -R cowrie /cowrie/cowrie-git/etc

# PROBLEM how to give cowrie the correct permissions
#RUN chmod +rwx /cowrie/cowrie-git/log/cowrie.json
RUN chown -R cowrie /cowrie/

# remove all the build tools to keep the image small
RUN apt-get remove -y --purge \
      git \
      python-pip \
      python-setuptools \
      libmpfr-dev \
      libssl-dev \
      libmpc-dev \
      libffi-dev \
      build-essential \
      libpython-dev && \

    # remove any auto-installed depends for the build and any temp files and package lists
    apt-get autoremove -y && \
    dpkg -l | awk '/^rc/ {print $2}' | xargs dpkg --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# baseimage start command
CMD ["/sbin/my_init"]

