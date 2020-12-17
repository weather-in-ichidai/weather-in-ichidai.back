# ベースイメージの指定
FROM python:3.7-buster as builder

WORKDIR /opt/app

COPY requirements.lock /opt/app
RUN pip3 install -r requirements.lock

# ここからは実行用コンテナの準備
FROM python:3.7-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

RUN apt update \
  && apt install -y libpq5 libxml2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get install -y cron

RUN useradd -r -s /bin/false uwsgiusr
RUN mkdir -p /opt/app/src/logs/app_logs
RUN touch /opt/app/src/logs/server.log
RUN chown -R uwsgiusr /opt/app/src/logs

COPY deploy/uwsgi.ini /opt/app
COPY src /opt/app/weather_in_ichidai

USER uwsgiusr

EXPOSE 8000
CMD ["uwsgi", "--ini", "/opt/app/uwsgi.ini"]