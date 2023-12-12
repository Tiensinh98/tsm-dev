import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tsm_project.settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class MyTestAppAPITests(APITestCase):
    def test_projects(self):
        # Define the URL for the API endpoint
        url = reverse('projects')

        # Make a GET request to the API endpoint with the 'name' parameter
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data
        self.assertEqual(response.json(), [
            {'id': 20, 'issue_name': 'Project 2', 'start_date': '2023-12-09', 'due_date': '2024-06-10', 'priority': 'medium', 'status': 'in_development', 'description': None, 'baseissue_ptr_id': 20, 'project_leader_id': 35},
            {'id': 19, 'issue_name': 'Project 1', 'start_date': '2023-12-09', 'due_date': None, 'priority': 'highest', 'status': 'to_do', 'description': None, 'baseissue_ptr_id': 19, 'project_leader_id': 33},
            {'id': 23, 'issue_name': 'Project 3', 'start_date': '2022-08-24', 'due_date': '2023-08-24', 'priority': 'highest', 'status': 'in_development', 'description': None, 'baseissue_ptr_id': 23, 'project_leader_id': 33},
            {'id': 25, 'issue_name': '', 'start_date': None, 'due_date': None, 'priority': 'medium', 'status': 'to_do', 'description': None, 'baseissue_ptr_id': 25, 'project_leader_id': None}
        ])
