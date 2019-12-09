FROM python:3.8-slim

LABEL maintainer = "Javier Salvador García  <javiersalvadorgarcia94@gmail.com>"

ENV ROCKET_URL ""
ENV ROCKET_CHANNEL_ID "" 
ENV ROCKET_LOGIN ""
ENV ROCKET_PASSWORD "" 
ENV TELEGRAM_BOT_TOKEN "" 
ENV TELEGRAM_CHANNEL_ID ""

RUN apt-get update \
    && apt-get -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade -yq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install requests \
    && pip3 install rocketchat_API

COPY telerocket.py /telerocket.py
CMD [ "python", "/telerocket.py" ]