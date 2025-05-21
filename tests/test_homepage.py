import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_homepage(client):
    url = reverse("home")  # у skeletonʼі це path('', home, name='home')
    response = client.get(url)
    assert response.status_code == 200
    assert b"It works!" in response.content
