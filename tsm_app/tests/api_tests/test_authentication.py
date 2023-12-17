from rest_framework import status


class TestAuthenticationAPIs:

    @staticmethod
    def test_register_and_login(api_test_case, basic_client):
        # Define the URL for the API endpoint

        # Make a GET request to the API endpoint with the 'name' parameter
        response = basic_client.post('/api/register/', {
            'username': 'andrew@gmail.com',
            'password': '123456'
        })

        # Check that the response status code is 200 (OK)
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data
        api_test_case.assertEqual(response.json(), {'success': True, 'message': 'Create User successfully'})

        response = basic_client.post('/api/login/', {
            'username': 'andrew@gmail.com',
            'password': '123456'
        })
        api_test_case.assertEqual(response.json(), {'success': True})
