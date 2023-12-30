from django.urls import reverse
from rest_framework import status


class TestIssueAPIs:

    @staticmethod
    def test_project_api_1(api_test_case, super_client, dataset):
        init_project_data = [
            {'id': 1, 'name': 'Project 1', 'start_date': '2023-12-17', 'due_date': '2023-12-17',
             'priority': 'medium', 'status': 'in_development', 'description': None, 'leader_id': 1},
            {'id': 2, 'name': 'Project 2', 'start_date': '2023-12-17', 'due_date': '2023-12-17',
             'priority': 'medium', 'status': 'to_do', 'description': None, 'leader_id': None}
        ]
        response = super_client.get('/api/projects/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), init_project_data)
        #
        response = super_client.get('/api/projects/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {
            'id': 2, 'name': 'Project 2', 'start_date': '2023-12-17', 'due_date': '2023-12-17', 'priority': 'medium', 'status': 'to_do', 'description': None, 'leader_id': None
        })

        response = super_client.post('/api/projects/add/', {
            'id': 3,
            'name': 'Project 3',
            'start_date': '2023-12-22',
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        api_test_case.assertEqual(response.json(), {'message': f'Create Project successfully'})
        init_project_data.append(
            {'id': 3, 'name': 'Project 3', 'start_date': '2023-12-22', 'due_date': None,
             'priority': 'medium', 'status': 'to_do', 'description': None, 'leader_id': None})
        response = super_client.get('/api/projects/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), init_project_data)
        #
        response = super_client.delete('/api/projects/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Delete Project successfully'})
        response = super_client.get('/api/projects/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        init_project_data.pop(1)
        api_test_case.assertEqual(response.json(), init_project_data)
        #
        response = super_client.patch('/api/projects/3/', {
            'start_date': '2023-02-10',
            'leader_id': 2
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['id'], 3)
        api_test_case.assertEqual(response.json()['start_date'], '2023-02-10')
        api_test_case.assertEqual(response.json()['leader_id'], 2)
        #
        response = super_client.post('/api/projects/add/', {
            'id': 4,
            'name': 'Project 4',
            'start_date': '2023-01-01',
            'leader_id': 2
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        api_test_case.assertEqual(response.json(), {'message': f'Create Project successfully'})
        response = super_client.get('/api/projects/filter/', {
            'leader_id': 2
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [
            {'id': 3, 'name': 'Project 3', 'start_date': '2023-02-10', 'due_date': None,
             'priority': 'medium', 'status': 'to_do', 'description': None, 'leader_id': 2},
            {'id': 4, 'name': 'Project 4', 'start_date': '2023-01-01', 'due_date': None,
             'priority': 'medium', 'status': 'to_do', 'description': None, 'leader_id': 2}])
        response = super_client.get('/api/projects/filter/', {
            'leader_id': 2,
            'start_date__gt': '2023-02-09'
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [
            {'id': 3, 'name': 'Project 3', 'start_date': '2023-02-10', 'due_date': None,
             'priority': 'medium', 'status': 'to_do', 'description': None, 'leader_id': 2}
        ])
