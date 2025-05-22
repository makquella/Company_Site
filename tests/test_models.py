import pytest
from core.models import Service


@pytest.mark.django_db
def test_service_str():
    s = Service.objects.create(title="SEO Audit", slug="seo-audit")
    assert str(s) == "SEO Audit"
