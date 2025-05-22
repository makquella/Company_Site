import pytest
from django.urls import reverse
from core.models import ContactRequest


@pytest.mark.django_db
def test_can_submit_contact(client):
    url = reverse("contact")
    data = {
        "name": "John Doe",
        "email": "john@example.com",
        "subject": "Need help",
        "message": "Call me, please",
    }
    resp = client.post(url, data, follow=True)
    assert resp.status_code == 200
    assert ContactRequest.objects.filter(email="john@example.com").exists()
