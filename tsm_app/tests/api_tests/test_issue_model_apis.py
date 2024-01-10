from rest_framework import status


class TestIssueAPIs:

    @staticmethod
    def test_project_api_1(api_test_case, super_client, dataset):
        init_project_data = [
            {
                "id": 1,
                "name": 'Project 1',
                "startDate": '2023-12-17',
                "dueDate": '2023-12-17',
                "priority": 'medium',
                "status": 'in_development',
                "description": None,
                "leader": {
                    'id': 1,
                    'firstName': 'Test',
                    'lastName': 'User'
                }
            },
            {
                'id': 2,
                'name': 'Project 2',
                'startDate': '2023-12-17',
                'dueDate': '2023-12-17',
                'priority': 'medium',
                'status': 'to_do',
                'description': None,
                'leader': None
            }
        ]
        response = super_client.get('/api/projects/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), init_project_data)
        #
        response = super_client.get('/api/projects/10/')
        api_test_case.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        api_test_case.assertEqual(response.json(), {'message': 'Project not found'})
        response = super_client.get('/api/projects/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {
            'id': 2,
            'name': 'Project 2',
            'startDate': '2023-12-17',
            'dueDate': '2023-12-17',
            'priority': 'medium',
            'status': 'to_do',
            'description': None,
            'leader': None
        })
        # generate csrf token
        response = super_client.get('/api/csrf-token/')
        csrf_token = response.json().get('csrfToken')
        #
        response = super_client.post('/api/projects/add/', {
            'id': 3,
            'name': 'Project 3',
            'startDate': '2023-12-22',
        }, HTTP_X_CSRFTOKEN=csrf_token)
        api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        api_test_case.assertEqual(response.json(), {'message': f'Create Project successfully'})
        init_project_data.append(
            {
                'id': 3,
                'name': 'Project 3',
                'startDate': '2023-12-22',
                'dueDate': None,
                'priority': 'medium',
                'status': 'to_do',
                'description': None,
                'leader': None
            })
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
            'startDate': '2023-02-10',
            "leader": 2
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['id'], 3)
        api_test_case.assertEqual(response.json()['startDate'], '2023-02-10')
        api_test_case.assertEqual(response.json()['leader'], {
            "id": 2,
            "firstName": 'Test',
            "lastName": 'User1'
        })
        #
        response = super_client.post('/api/projects/add/', {
            'id': 4,
            'name': 'Project 4',
            'startDate': '2023-01-01',
            "leader": 2
        }, HTTP_X_CSRFTOKEN=csrf_token)
        api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        api_test_case.assertEqual(response.json(), {'message': f'Create Project successfully'})
        response = super_client.get('/api/projects/filter/', {
            "leader": 2
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [
            {
                "id": 3,
                "name": 'Project 3',
                "startDate": '2023-02-10',
                "dueDate": None,
                "priority": 'medium',
                "status": 'to_do',
                "description": None,
                "leader": {
                    "id": 2,
                    "firstName": 'Test',
                    "lastName": 'User1'
                }
            },
            {
                "id": 4,
                "name": 'Project 4',
                "startDate": '2023-01-01',
                "dueDate": None,
                "priority": 'medium',
                "status": 'to_do',
                "description": None,
                "leader": {
                    "id": 2,
                    "firstName": 'Test',
                    "lastName": 'User1'
                }
            }
        ])
        response = super_client.get('/api/projects/filter/', {
            'leader': 2,
            'start_date__gt': '2023-02-09'
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [
            {
                'id': 3,
                'name': 'Project 3',
                'startDate': '2023-02-10',
                'dueDate': None,
                'priority': 'medium',
                'status': 'to_do',
                'description': None,
                "leader": {
                    'id': 2,
                    'firstName': 'Test',
                    'lastName': 'User1'
                }
            }
        ])

    @staticmethod
    def test_task_api_1(api_test_case, super_client, dataset):
        init_task_data = [
            {
                'id': 3,
                'name': 'Task 1',
                'startDate': '2023-12-17',
                'dueDate': '2023-12-17',
                'priority': 'medium',
                'status': 'in_development',
                'description': None,
                'lineProject': {
                    'name': 'Project 1',
                    'id': 1, 'leader': {
                        'id': 1,
                        'firstName': 'Test',
                        'lastName': 'User'
                    }
                },
                'assignee': None
            },
            {
                'id': 4,
                'name': 'Task 2',
                'startDate': '2023-12-17',
                'dueDate': '2023-12-17',
                'priority': 'medium',
                'status': 'to_do',
                'description': None,
                'lineProject': {
                    'name': 'Project 1',
                    'id': 1,
                    'leader': {
                        'id': 1,
                        'firstName': 'Test',
                        'lastName': 'User'
                    }
                },
                'assignee': {
                    'id': 2,
                    'firstName': 'Test',
                    'lastName': 'User1'
                }
            }
        ]
        response = super_client.get('/api/tasks/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), init_task_data)
        #
        response = super_client.get('/api/tasks/10/')
        api_test_case.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        api_test_case.assertEqual(response.json(), {'message': 'Task not found'})
        response = super_client.get('/api/tasks/4/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), init_task_data[1])

        # generate csrf token
        response = super_client.get('/api/csrf-token/')
        csrf_token = response.json().get('csrfToken')
        #
        response = super_client.post('/api/tasks/add/', {
            'id': 5,
            'name': 'Task 3',
            'startDate': '2023-12-22',
            'lineProject': 2,
            'assignee': 1
        }, HTTP_X_CSRFTOKEN=csrf_token)
        api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        api_test_case.assertEqual(response.json(), {'message': f'Create Task successfully'})
        init_task_data.append(
            {
                'id': 5,
                'name': 'Task 3',
                'startDate': '2023-12-22',
                'dueDate': None,
                'priority': 'medium',
                'status': 'to_do',
                'description': None,
                'lineProject': {
                    'name': 'Project 2',
                    'id': 2,
                    'leader': None
                },
                'assignee': {
                    'id': 1,
                    'firstName': 'Test',
                    'lastName': 'User'
                }
            })
        response = super_client.get('/api/tasks/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), init_task_data)
        #
        response = super_client.delete('/api/tasks/4/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Delete Task successfully'})
        response = super_client.get('/api/tasks/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        init_task_data.pop(1)
        api_test_case.assertEqual(response.json(), init_task_data)
        #
        response = super_client.patch('/api/tasks/3/', {
            'startDate': '2022-02-10',
            'dueDate': '2022-10-10',
            'description': 'This is task 3',
            'assignee': 2
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['id'], 3)
        api_test_case.assertEqual(response.json()['startDate'], '2022-02-10')
        api_test_case.assertEqual(response.json()['dueDate'], '2022-10-10')
        api_test_case.assertEqual(response.json()['description'], 'This is task 3')
        api_test_case.assertEqual(response.json()['assignee'], {
            'id': 2, 'firstName': 'Test', 'lastName': 'User1'})
        #
        response = super_client.post('/api/tasks/add/', {
            'id': 4,
            'name': 'Task 2',
            'startDate': '2023-12-17',
            'dueDate': '2023-12-17',
            'priority': 'medium',
            'status': 'to_do',
            'description': None,
            'lineProject': 1,
            'assignee': 2
        }, HTTP_X_CSRFTOKEN=csrf_token)
        api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        api_test_case.assertEqual(response.json(), {'message': f'Create Task successfully'})
        response = super_client.get('/api/tasks/filter/', {
            'line_project': 1,
            'assignee': 1
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [])
        response = super_client.get('/api/tasks/filter/', {
            'line_project': 1,
            'due_date__lt': '2023-01-09'
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), [
            {
                'id': 3,
                'name': 'Task 1',
                'startDate': '2022-02-10',
                'dueDate': '2022-10-10',
                'priority': 'medium',
                'status': 'in_development',
                'description': 'This is task 3',
                'lineProject': {
                    'name': 'Project 1',
                    'id': 1,
                    'leader': {
                        'id': 1,
                        'firstName': 'Test',
                        'lastName': 'User'
                    }
                },
                'assignee': {
                    'id': 2,
                    'firstName': 'Test',
                    'lastName': 'User1'
                }
            }
        ])
