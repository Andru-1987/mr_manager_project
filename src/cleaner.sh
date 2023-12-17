#!/usr/bin/sh


deactivate

rm -rf venv

rm -rf ./src/*/*/*pycache*
rm -rf ./src/*/*pycache*
rm -rf ./src/*/migrations/000*
rm -rf ./src/*.sqlite*
rm -rf ./src/media/*



# python -m venv venv && source ./venv/bin/activate && pip install -r ./src/requirements.txt

# python ./src/manage.py makemigrations
# python ./src/manage.py migrate

# DJANGO_SUPERUSER_PASSWORD=admin \
# DJANGO_SUPERUSER_USERNAME=1111 \
# DJANGO_SUPERUSER_EMAIL=admin@domain.com \
# ./src/manage.py createsuperuser \
# --dni 1111 --no-input

# python ./src/manage.py runserver 5000

# postgresql
