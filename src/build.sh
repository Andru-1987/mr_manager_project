#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

mkdir  staticfiles media

# python manage.py sqlflush # solo por para propositos generales de deploy

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

DJANGO_SUPERUSER_USERNAME=11111111 \
DJANGO_SUPERUSER_PASSWORD=admin \
DJANGO_SUPERUSER_EMAIL="mail_admin@mail.com" \
python manage.py createsuperuser --dni 11111111 --noinput
