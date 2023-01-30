#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"














#sleep 10

#python manage.py migrate --noinput
#gunicorn tdolist.wsgi:application --bind 0.0.0.0:8000
#
##python manage.py migrate
##python manage.py createcachetable
##python manage.py collectstatic  --noinput
##gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
#
#exec "$@"


