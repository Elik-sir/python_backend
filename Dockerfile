FROM ubuntu:latest
MAINTAINER Eldar 'eldar@gmail.com'
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ['python']
CMD ['main.py']