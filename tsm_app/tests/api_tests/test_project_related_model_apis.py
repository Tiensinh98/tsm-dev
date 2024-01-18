import datetime
import pytest
from rest_framework import status


class TestProjectAPIs:

    @staticmethod
    @pytest.mark.django_db
    def test_task_of_project(api_test_case, super_client, dataset):
        tasks_of_project = [
            {
                'id': 3,
                'name': 'Task 1',
                'startDate': '2023-12-17',
                'dueDate': '2023-12-17',
                'createdDate': str(datetime.date.today()),
                'priority': 'medium',
                'status': 'in_development',
                'description': None,
                'lineProject': {
                    'name': 'Project 1',
                    'id': 1, 'leader': {'id': 1, 'firstName': 'Test', 'lastName': 'User'}},
                'assignee': None
            },
            {
                'id': 4,
                'name': 'Task 2',
                'startDate': '2023-12-17',
                'dueDate': '2023-12-17',
                'createdDate': str(datetime.date.today()),
                'priority': 'medium',
                'status': 'to_do',
                'description': None,
                'lineProject': {
                    'name': 'Project 1',
                    'id': 1, 'leader': {'id': 1, 'firstName': 'Test', 'lastName': 'User'}},
                'assignee': {'id': 2, 'firstName': 'Test', 'lastName': 'User1'}
            }
        ]
        response = super_client.get('/api/projects/1/tasks/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), tasks_of_project)
        response = super_client.get('/api/projects/1/tasks/filter/', {
            'assignee': 2
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), tasks_of_project[1:])
        response = super_client.get('/api/projects/1/tasks/filter/', {
            'status': "to_do"
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), tasks_of_project[1:])
        response = super_client.get('/api/projects/1/tasks/filter/', {
            'assignee': 1,
            'status': "to_do"
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [])

    @staticmethod
    @pytest.mark.django_db
    def test_device_of_project(api_test_case, super_client, dataset):
        response = super_client.get('/api/projects/1/devices/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)


    @staticmethod
    @pytest.mark.django_db
    def test_user_of_project(api_test_case, super_client, dataset):
        response = super_client.get('/api/projects/1/users/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        project_1_related_user = {
            'leader':
                {'id': 1, 'email': 'test@akselos.com',
                 'username': 'test_user', 'firstName': 'Test', 'lastName': 'User'},
            'assignees': [
                {'id': 2, 'email': 'test1@example.com',
                 'username': 'test_user1', 'firstName': 'Test', 'lastName': 'User1'}
            ]
        }
        api_test_case.assertEqual(response.json(), project_1_related_user)
        response = super_client.get('/api/projects/1/users/filter/', {
            'id': 2
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {
            'leader': None,
            "assignees": project_1_related_user['assignees']
        })
        response = super_client.get('/api/projects/1/users/filter/', {
            "email__contains": "akselos"
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {
            'leader': {'id': 1, 'email': 'test@akselos.com',
                       'username': 'test_user', 'firstName': 'Test', 'lastName': 'User'},
            'assignees': []
        })
