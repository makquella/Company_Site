#!/usr/bin/env sh
# Exit on error
set -e

python manage.py migrate --noinput

python manage.py collectstatic --noinput

exec "$@"
