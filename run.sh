#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py createsuperuser --no-input
gunicorn project.wsgi --bind=0.0.0.0:$PORT
