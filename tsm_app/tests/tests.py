import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tsm_project.settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class ProjectAPITests(APITestCase):

    def test_get_projects(self):
        # Define the URL for the API endpoint
        url = reverse('projects')

        # Make a GET request to the API endpoint with the 'name' parameter
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data
        self.assertEqual(response.json(), [
            {'id': 20, 'issue_name': 'Project 2', 'start_date': '2023-12-09', 'due_date': '2023-12-09', 'priority': 'medium', 'status': 'in_development', 'description': None, 'project_leader': {'id': 35, 'first_name': 'Phuong', 'last_name': 'Huynh', 'dob': None, 'role': 'senior_software_engineer'}, 'workers': []},
            {'id': 19, 'issue_name': 'Project 1', 'start_date': '2023-12-09', 'due_date': '2023-12-09', 'priority': 'highest', 'status': 'to_do', 'description': None, 'project_leader': {'id': 33, 'first_name': 'John', 'last_name': 'Bell', 'dob': None, 'role': 'senior_software_developer'}, 'workers': []},
            {'id': 23, 'issue_name': 'Project 3', 'start_date': '2022-08-24', 'due_date': '2022-08-24', 'priority': 'highest', 'status': 'in_development', 'description': None, 'project_leader': {'id': 33, 'first_name': 'John', 'last_name': 'Bell', 'dob': None, 'role': 'senior_software_developer'}, 'workers': []},
            {'id': 25, 'issue_name': '', 'start_date': None, 'due_date': None, 'priority': 'medium', 'status': 'to_do', 'description': None, 'project_leader': None, 'workers': []}])

    def test_get_project(self):
        # Define the URL for the API endpoint

        # Make a GET request to the API endpoint with the 'name' parameter
        response = self.client.get('/projects/20/')

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data
        self.assertEqual(response.json(), {
            'id': 20, 'issue_name': 'Project 2', 'start_date': '2023-12-09', 'due_date': '2023-12-09', 'priority': 'medium', 'status': 'in_development', 'description': None,
            'project_leader': {'id': 35, 'first_name': 'Phuong', 'last_name': 'Huynh', 'dob': None, 'role': 'senior_software_engineer'},
            'workers': []})

    def test_add_project(self):
        # Define the URL for the API endpoint

        # Make a GET request to the API endpoint with the 'name' parameter
        response = self.client.post('/projects/add/', {
            'issue_name': 'Project 4',
            'start_date': '2023-12-22',
            'project_leader': 33
        })

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the response contains the expected data
        self.assertEqual(response.json(), {'message': f'Create Project successfully'})

    def test_delete_project(self):
        # Define the URL for the API endpoint

        # Make a GET request to the API endpoint with the 'name' parameter
        response = self.client.delete('/projects/20/')

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data
        self.assertEqual(response.json(), {'message': 'Delete Project successfully'})

    def test_update_project(self):
        # Make a GET request to the API endpoint with the 'name' parameter
        response = self.client.patch('/projects/20/', {
            'issue_name': 'Project 5'
        })

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data
        self.assertEqual(response.json(), {
            'id': 20,
            'issue_name': 'Project 5',
            'start_date': '2023-12-09',
            'due_date': '2023-12-09',
            'priority': 'medium',
            'status': 'in_development',
            'description': None,
            'project_leader': {'id': 35, 'first_name': 'Phuong', 'last_name': 'Huynh', 'dob': None, 'role': 'senior_software_engineer'},
            'workers': []})

    def test_filter_projects(self):
        # Define the URL for the API endpoint

        # Make a GET request to the API endpoint with the 'name' parameter
        response = self.client.get('/projects/filter/', {
            'priority': 'medium'
        })

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data
        self.assertEqual(response.json(), [
            {'id': 20, 'issue_name': 'Project 2', 'start_date': '2023-12-09', 'due_date': '2023-12-09', 'priority': 'medium', 'status': 'in_development', 'description': None, 'project_leader': {'id': 35, 'first_name': 'Phuong', 'last_name': 'Huynh', 'dob': None, 'role': 'senior_software_engineer'}, 'workers': []},
            {'id': 25, 'issue_name': '', 'start_date': None, 'due_date': None, 'priority': 'medium', 'status': 'to_do', 'description': None, 'project_leader': None, 'workers': []}])