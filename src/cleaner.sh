#!/usr/bin/sh
 
rm -rf */*/*pycache*
rm -rf */*pycache*
rm -rf */migrations/000*
rm -rf *.sqlite*
rm -rf media/*

# python manage.py makemigrations
# python manage.py migrate

DJANGO_SUPERUSER_PASSWORD=admin \
DJANGO_SUPERUSER_USERNAME=1111 \
DJANGO_SUPERUSER_EMAIL=admin@domain.com \
./manage.py createsuperuser \
--dni 1111 --no-input

# python manage.py runserver 5000

# postgresql