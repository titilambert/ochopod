FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive

#
# - update our repo
# - add python 2.7 + some utilities
#
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install curl python supervisor

#
# - add the ochopod package and install it
# - remove defunct packages
# - start supervisor
#
ADD resources/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
# TODO change this line to link to the master repo/branch
RUN pip install git+https://github.com/titilambert/ochopod.git@more_pythonic
RUN apt-get -y autoremove
CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
