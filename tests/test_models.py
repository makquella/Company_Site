import pytest
from django.apps import apps

def test_models_exist():
    expected_apps = ['core', 'services', 'crm', 'blog']
    for app_label in expected_apps:
        assert apps.is_installed(app_label)