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
    def test_device_of_project(api_test_case, super_client, dataset2):
        initial_device_of_project = [
            {
                'id': 1,
                'deviceName': 'Device 1',
                'deviceType': 'laptop',
                'purchaseDate': '2024-01-20',
                'supplier': 'PV',
                'invoice': 'device_1.png',
                'handoverDate': '2024-01-20',
                'basicConfig': '',
                'status': 'in_use',
                'project': {
                    'name': 'Project 2',
                    'id': 2,
                    'leader': None
                }
            },
            {
                'id': 2,
                'deviceName': 'Device 2',
                'deviceType': 'laptop',
                'purchaseDate': '2024-01-20',
                'supplier': 'FPT',
                'invoice': 'device_2.png',
                'handoverDate': '2024-01-20',
                'basicConfig': '',
                'status': 'in_use',
                'project': {
                    'name': 'Project 2',
                    'id': 2,
                    'leader': None
                }
            }
        ]
        response = super_client.get('/api/projects/2/devices/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), initial_device_of_project)
        #
        response = super_client.patch('/api/projects/2/devices/add/3/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Add device to project successfully'})
        initial_device_of_project.append({
            'id': 3,
            'deviceName': 'Device 3',
            'deviceType': 'laptop',
            'purchaseDate': '2024-01-20',
            'supplier': 'FPT',
            'invoice': 'device_3.png',
            'handoverDate': '2024-01-20',
            'basicConfig': '',
            'status': 'in_use',
            'project': {
                'name': 'Project 2',
                'id': 2, 'leader': None
            }
        })
        response = super_client.get('/api/projects/2/devices/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), initial_device_of_project)
        # delete device from project
        response = super_client.delete('/api/projects/2/devices/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'success': 'Delete Project of device successfully'})
        initial_device_of_project.pop(1)
        response = super_client.get('/api/projects/2/devices/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), initial_device_of_project)
        #
        response = super_client.patch('/api/projects/1/devices/add/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Add device to project successfully'})
        response = super_client.get('/api/projects/1/devices/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [
            {
                'id': 2,
                'deviceName': 'Device 2',
                'deviceType': 'laptop',
                'purchaseDate': '2024-01-20',
                'supplier': 'FPT',
                'invoice': 'device_2.png',
                'handoverDate': '2024-01-20',
                'basicConfig': '',
                'status': 'in_use',
                'project': {
                    'name': 'Project 1',
                    'id': 1,
                    'leader': None
                }
            }
        ])

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
        # get all tasks before
        response = super_client.get('/api/projects/1/tasks/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()[1]['assignee'], {
            'id': 2,
            'firstName': 'Test',
            'lastName': 'User1'
        })
        # remove user-related things from project
        response = super_client.delete('/api/projects/1/users/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'success': 'Update all things related to user successfully'})
        #
        response = super_client.get('/api/projects/1/users/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {
            'leader':
                {'id': 1, 'email': 'test@akselos.com',
                 'username': 'test_user', 'firstName': 'Test', 'lastName': 'User'},
            'assignees': []
        })
        response = super_client.get('/api/projects/1/tasks/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()[1]['assignee'], None)
