import pytest
from rest_framework import status


class TestTeamAPIs:

    @staticmethod
    @pytest.mark.django_db
    def test_user_of_team(api_test_case, super_client, dataset1):
        people_of_team_2 = {
            'leader': {
                'id': 2,
                'email': 'test1@gmail.com',
                'username': 'test_user1',
                'firstName': 'Test',
                'lastName': 'User1'
            },
            'members': [
                {
                    'id': 3,
                    'email': 'andree@gmail.com',
                    'username': 'andree',
                    'firstName': 'Andree',
                    'lastName': 'Right Hand'
                },
                {
                    'id': 4,
                    'email': 'binz@akselos.com',
                    'username': 'binz',
                    'firstName': 'Binz',
                    'lastName': 'Badboiz'
                }
            ]
        }
        response = super_client.get('/api/teams/2/people/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), people_of_team_2)
        #
        people_of_team_1 = {
            'leader': {
                'id': 1,
                'email': 'test@akselos.com',
                'username': 'test_user',
                'firstName': 'Test',
                'lastName': 'User'
            },
            'members': []
        }
        response = super_client.get('/api/teams/1/people/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), people_of_team_1)
        #
        response = super_client.get('/api/teams/3/people/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {"leader": None, "members": []})
        response = super_client.get('/api/teams/2/people/filter/', {
            'id': 3
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {
            'leader': None,
            'members': [
                {
                    'id': 3,
                    'email': 'andree@gmail.com',
                    'username': 'andree',
                    'firstName': 'Andree',
                    'lastName': 'Right Hand'
                }
            ]
        })
        response = super_client.get('/api/teams/2/people/filter/', {
            "email__contains": "gmail.com"
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {
            'leader': {
                'id': 2,
                'email': 'test1@gmail.com',
                'username': 'test_user1',
                'firstName': 'Test',
                'lastName': 'User1'
            },
            'members': [
                {
                    'id': 3,
                    'email': 'andree@gmail.com',
                    'username': 'andree',
                    'firstName': 'Andree',
                    'lastName': 'Right Hand'
                }
            ]
        })

    @staticmethod
    @pytest.mark.django_db
    def test_add_remove_user_of_team(api_test_case, super_client, dataset1):
        people_of_team_2 = {
            'leader': {
                'id': 2,
                'email': 'test1@gmail.com',
                'username': 'test_user1',
                'firstName': 'Test',
                'lastName': 'User1'
            },
            'members': [
                {
                    'id': 3,
                    'email': 'andree@gmail.com',
                    'username': 'andree',
                    'firstName': 'Andree',
                    'lastName': 'Right Hand'
                },
                {
                    'id': 4,
                    'email': 'binz@akselos.com',
                    'username': 'binz',
                    'firstName': 'Binz',
                    'lastName': 'Badboiz'
                }
            ]
        }
        response = super_client.get('/api/teams/2/people/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), people_of_team_2)
        #
        response = super_client.delete('/api/teams/2/people/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Remove leader from team'})
        response = super_client.get('/api/teams/2/people/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['leader'], None)
        api_test_case.assertEqual(response.json()['members'], [
            {
                'id': 3,
                'email': 'andree@gmail.com',
                'username': 'andree',
                'firstName': 'Andree',
                'lastName': 'Right Hand'
            },
            {
                'id': 4,
                'email': 'binz@akselos.com',
                'username': 'binz',
                'firstName': 'Binz',
                'lastName': 'Badboiz'
            }
        ])
        #
        response = super_client.delete('/api/teams/2/people/3/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Remove a member from team'})
        response = super_client.get('/api/teams/2/people/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['leader'], None)
        api_test_case.assertEqual(response.json()['members'], [
            {
                'id': 4,
                'email': 'binz@akselos.com',
                'username': 'binz',
                'firstName': 'Binz',
                'lastName': 'Badboiz'
            }
        ])
        # add leader and members back to the team
        response = super_client.patch('/api/teams/2/people/add-leader/2/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Change leader successfully'})
        response = super_client.get('/api/teams/2/people/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['leader'], {
            'id': 2,
            'email': 'test1@gmail.com',
            'username': 'test_user1',
            'firstName': 'Test',
            'lastName': 'User1'
        })
        #
        response = super_client.patch('/api/teams/2/people/add-member/3/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'message': 'Add a member from team'})
        response = super_client.get('/api/teams/2/people/')
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json()['members'], [
            {
                'id': 4,
                'email': 'binz@akselos.com',
                'username': 'binz',
                'firstName': 'Binz',
                'lastName': 'Badboiz'
            },
            {
                'id': 3,
                'email': 'andree@gmail.com',
                'username': 'andree',
                'firstName': 'Andree',
                'lastName': 'Right Hand'
            }
        ])
