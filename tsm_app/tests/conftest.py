import pytest
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tsm_project.settings")
os.environ.setdefault('TSM_APP_SETTINGS', 'test_app_config.json')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from rest_framework.test import APIClient

@pytest.fixture(autouse=True)
def client():
    return APIClient()
