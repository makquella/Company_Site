import pytest
from html import unescape


@pytest.mark.django_db
def test_homepage(client):
    response = client.get("/")  # або reverse("home") у другому файлі
    assert response.status_code == 200

    html = unescape(response.content.decode()).replace("\u00a0", " ")
    assert "Better Solutions For Your Business" in html
