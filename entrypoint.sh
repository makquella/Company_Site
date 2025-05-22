#!/usr/bin/env sh
set -e

python manage.py migrate

exec gunicorn company_site.wsgi:application --bind 0.0.0.0:8000