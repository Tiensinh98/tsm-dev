from rest_framework import status
import datetime


class TestProjectAPIs:

    @staticmethod
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
    def test_device_of_project(api_test_case, super_client, dataset):
        response = super_client.get('/api/projects/1/devices/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)


    @staticmethod
    def test_user_of_project(api_test_case, super_client, dataset):
        response = super_client.get('/api/projects/1/users/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)

        response = super_client.get('/api/projects/1/users/filter/', {
            "last_name__contains": "1"
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
