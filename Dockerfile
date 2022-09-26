# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /usr/src/app
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV JWT-PRIVATE-KEY="YOUR-KEY-HERE"
#Server will reload itself on file changes if in dev mode
ENV FLASK_DEBUG=1 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run"]