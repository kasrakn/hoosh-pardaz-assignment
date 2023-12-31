#!/bin/sh

python manage.py migrate
python manage.py populate_data
python manage.py collectstatic --no-input --clear

exec "$@"