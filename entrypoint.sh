#!/bin/sh

sleep 10

python manage.py migrate --noinput
gunicorn tdolist.wsgi:application --bind 0.0.0.0:8000

#python manage.py migrate
#python manage.py createcachetable
#python manage.py collectstatic  --noinput
#gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000

exec "$@"


