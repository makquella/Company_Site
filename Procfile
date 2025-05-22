release: python manage.py migrate --noinput

web: gunicorn company_site.wsgi:application --log-file -