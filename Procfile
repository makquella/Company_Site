﻿release: python manage.py migrate --noinput

web: gunicorn company_site.wsgi:application --bind 0.0.0.0:$PORT