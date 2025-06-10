# Company Site Skeleton

This repository contains a minimal Django project prepared for the **“standard”** level of the CI/CD laboratory work.

## Quick start

```bash
git clone <your_repo_url>
cd Company_Site
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Run tests

```bash
pytest
```

### Build & run with Docker

```bash
docker-compose up --build
```

## CI

A ready‑made GitHub Actions workflow is placed in `.github/workflows/ci.yml`.
