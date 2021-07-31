FROM python:3
RUN pip install --upgrade pip
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential libzbar0
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
