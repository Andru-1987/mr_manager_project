#!/usr/bin/sh


mkdir media staticfiles

python manage.py makemigrations 
python manage.py migrate 
python manage.py collectstatic --noinput


DJANGO_SUPERUSER_USERNAME=11111111 \
DJANGO_SUPERUSER_PASSWORD=admin \
DJANGO_SUPERUSER_EMAIL="andru.ocatorres@gmail.com" \
python manage.py createsuperuser --dni 11111111 --noinput

gunicorn aigasra_project.wsgi:application --bind "0.0.0.0:8000"

