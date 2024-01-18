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
