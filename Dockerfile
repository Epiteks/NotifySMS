FROM python:3.5-alpine

MAINTAINER hug33k

ENV SMS_LOGIN login
ENV SMS_TOKEN token
ENV EPITECH_MAIL mail
ENV EPITECH_PWD pwd
ENV NOTIFYSMS_DIR /app

RUN echo "http://dl-2.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories; \
    echo "http://dl-3.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories; \
    echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories; \
    echo "http://dl-5.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

RUN apk update; apk add apk-cron

RUN mkdir /app

COPY . /app/

RUN crontab -l | cat - /app/crontab | crontab -

RUN touch /var/log/cron.log

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD crond && tail -f /var/log/cron.log
