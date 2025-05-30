FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ENTRYPOINT entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "company_site.wsgi:application", "--bind", "0.0.0.0:8000"]
