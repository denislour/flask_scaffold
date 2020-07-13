FROM python:3.8-alpine

ENV FLASK_APP craft.py
ENV FLASK_CONFIG docker

RUN adduser -D craft
USER craft

WORKDIR /home/craft
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY craft.py config.py boot.sh ./

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
