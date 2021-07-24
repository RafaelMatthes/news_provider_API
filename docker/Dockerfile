FROM python:3.8.3

# set work directory
WORKDIR /api

# RUN apt update && apt install -y python3-setuptools

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT python manage.py makemigrations --no-input && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# ENTRYPOINT  python manage.py runserver 0.0.0.0:8000