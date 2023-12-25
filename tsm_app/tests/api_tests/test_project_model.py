from django.urls import reverse
from rest_framework import status


class TestProjectAPI:

    @staticmethod
    def test_project_api_1(api_test_case, super_client, dataset):
        url = reverse('projects')
        response = super_client.get(url)
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [
            {'id': 2, 'issue_name': 'Project 2', 'start_date': '2023-12-17', 'due_date': '2023-12-17', 'priority': 'medium', 'status': 'in_development', 'description': None, 'project_leader': {'id': 3, 'first_name': 'Phuong', 'last_name': 'Huynh', 'dob': None, 'role': 'senior_software_engineer'}, 'workers': []},
            {'id': 1, 'issue_name': 'Project 1', 'start_date': '2023-12-17', 'due_date': '2023-12-17', 'priority': 'high', 'status': 'to_do', 'description': None, 'project_leader': {'id': 1, 'first_name': 'John', 'last_name': 'Bell', 'dob': None, 'role': 'senior_software_developer'}, 'workers': []}
        ])
        #
        response = super_client.get('/api/projects/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'id': 2, 'issue_name': 'Project 2', 'start_date': '2023-12-17', 'due_date': '2023-12-17', 'priority': 'medium', 'status': 'in_development', 'description': None, 'project_leader': {'id': 3, 'first_name': 'Phuong', 'last_name': 'Huynh', 'dob': None, 'role': 'senior_software_engineer'}, 'workers': []})
        #
        response = super_client.post('/api/projects/add/', {
            'issue_name': 'Project 3',
            'start_date': '2023-12-22',
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        api_test_case.assertEqual(response.json(), {'message': f'Create Project successfully'})
        #
        response = super_client.delete('/api/projects/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Delete Project successfully'})
        #
        response = super_client.patch('/api/projects/1/', {
            'start_date': '2023-07-17'
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['start_date'], '2023-07-17')
        api_test_case.assertEqual(response.json()['due_date'], '2023-12-17')
        #
        response = super_client.get('/api/projects/filter/', {
            'priority': 'high'
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [{
            'id': 1, 'issue_name': 'Project 1', 'start_date': '2023-07-17', 'due_date': '2023-12-17',
            'priority': 'high', 'status': 'to_do', 'description': None,
            'project_leader': {
                'id': 1, 'first_name': 'John', 'last_name': 'Bell',
                'dob': None, 'role': 'senior_software_developer'}, 'workers': []}])


class TestLeaderAPI:

    @staticmethod
    def test_leader_api_1(api_test_case, super_client, dataset):
        url = reverse('leaders')
        response = super_client.get(url)
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [
            {'id': 1, 'first_name': 'John', 'last_name': 'Bell', 'dob': '1992-05-17', 'role': 'senior_software_developer'},
            {'id': 3, 'first_name': 'Phuong', 'last_name': 'Huynh', 'dob': None, 'role': 'senior_software_developer'}
        ])
        #
        response = super_client.get('/api/leaders/1/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {
            "dob": "1992-05-17",
            "first_name": "John",
            "id": 1,
            "last_name": "Bell",
            "role": "senior_software_developer"
        })
        #
        response = super_client.post('/api/leaders/add/', {
            'first_name': 'Sinh',
            'last_name': 'Pham',
            "role": "senior_software_engineer"
        })
        created_leader_id = super_client.get(url).json()[-1]['id']
        api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        api_test_case.assertEqual(response.json(), {'message': f'Create Leader successfully'})
        #
        response = super_client.delete('/api/leaders/3/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Delete Leader successfully'})
        #
        response = super_client.patch('/api/leaders/1/', {
            'dob': '1997-02-19',
            "role": "senior_software_engineer"
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['dob'], '1997-02-19')
        #
        response = super_client.get('/api/leaders/filter/', {
            "role": "senior_software_engineer"
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [{
            'id': created_leader_id, 'first_name': 'Sinh', 'last_name': 'Pham', 'dob': None, 'role': 'senior_software_engineer'},
            {'id': 1, 'first_name': 'John', 'last_name': 'Bell', 'dob': '1997-02-19', 'role': 'senior_software_engineer'}
        ])