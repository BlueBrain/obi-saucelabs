FROM python:3.10

COPY entrypoint.sh /entrypoint.sh

RUN apt-get update
RUN apt-get install -y firefox-esr xvfb
RUN mkdir /gecko
WORKDIR /gecko
RUN wget "https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz"
RUN tar -xvzf geckodriver-v0.33.0-linux64.tar.gz
RUN chmod +x geckodriver
ENV PATH=/gecko:${PATH}
ENV DISPLAY=:99

ENTRYPOINT /entrypoint.sh
