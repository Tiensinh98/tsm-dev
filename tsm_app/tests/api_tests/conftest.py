import pytest
import pathlib

from rest_framework.test import APITestCase, APIClient
from tsm_app.app_tools import utils, database as db

TEST_DIR = pathlib.Path(__file__).resolve().parent.parent

@pytest.fixture(autouse=True)
def api_test_case():
    return APITestCase()

@pytest.fixture(autouse=True)
def super_client():
    utils.truncate_all_tables()
    user = db.CustomUser.objects.create_user(
        username='testuser', password='testpassword',
        is_superuser=True, email='test_user@gmail.com')
    client = APIClient(enforce_csrf_checks=True)
    client.force_authenticate(user=user)
    return client

@pytest.fixture(autouse=True)
def basic_client():
    utils.truncate_all_tables()
    db.CustomUser.objects.create_user(
        username='testuser', email='test_user@gmail.com',
        password='testpassword', is_superuser=False)
    return APIClient(enforce_csrf_checks=True)

@pytest.fixture(autouse=True)
def anonymous_client():
    utils.truncate_all_tables()
    return APIClient()

@pytest.fixture()
def dataset():
    utils.truncate_all_tables()
    dataset_filepath = TEST_DIR / 'test_datasets' / 'dataset_1.json'
    utils.read_dataset_from_json(dataset_filepath)

@pytest.fixture()
def dataset1():
    utils.truncate_all_tables()
    dataset_filepath = TEST_DIR / 'test_datasets' / 'test_team_related_dataset.json'
    utils.read_dataset_from_json(dataset_filepath)

@pytest.fixture()
def dataset2():
    utils.truncate_all_tables()
    dataset_filepath = TEST_DIR / 'test_datasets' / 'test_project_device_dataset.json'
    utils.read_dataset_from_json(dataset_filepath)
