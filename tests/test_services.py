import pytest
from django.urls import reverse
from core.models import Service


@pytest.mark.django_db
def test_services_page(client):
    Service.objects.create(
        title="Active Service", slug="active-service", is_active=True
    )
    Service.objects.create(
        title="Inactive Service", slug="inactive-service", is_active=False
    )
    url = reverse("services")
    resp = client.get(url)
    assert resp.status_code == 200
    assert b"Active Service" in resp.content
    assert b"Inactive Service" not in resp.content
