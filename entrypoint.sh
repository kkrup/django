#!/bin/sh bash

while ! nc -z db:5432; do sleep 1 && echo "Waiting"; done

python /code/manage.py makemigrations

python /code/manage.py migrate

python /code/manage.py runserver 0.0.0.0:8000
