import pytest
from django.urls import reverse
from core.models import Service


@pytest.mark.django_db
def test_services_page(client):
    Service.objects.create(title="SEO Audit", slug="seo-audit", is_active=True)
    url = reverse("services")
    resp = client.get(url)
    assert resp.status_code == 200
    assert b"SEO Audit" in resp.content
