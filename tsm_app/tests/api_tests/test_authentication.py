from rest_framework import status
from django.core import mail

class TestAuthenticationAPIs:

    @staticmethod
    def test_register_and_login_and_logout(api_test_case, basic_client):
        # Make a GET request to the API endpoint with the 'name' parameter
        response = basic_client.post('/api/register/', {
            'username': 'andrew',
            'email': 'andrew@gmail.com',
            'password': '123456'
        })

        # Check that the response status code is 200 (OK)
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data
        api_test_case.assertEqual(response.json(), {'success': True, 'message': 'Create User successfully'})

        response = basic_client.post('/api/login/', {
            'username': 'andrew',
            'password': '123456'
        })
        api_test_case.assertEqual(response.json(), {'success': True})
        response = basic_client.get('/api/csrf-token/')
        csrf_token = response.json().get('csrfToken') # or from response.cookies['csrftoken']
        response = basic_client.post('/api/logout/', HTTP_X_CSRFTOKEN=csrf_token)
        api_test_case.assertEqual(response.json(), {'success': True})

    def test_change_password(self, api_test_case, basic_client):
        response = basic_client.post('/api/register/', {
            'email': 'andrew@gmail.com',
            'username': 'andrew',
            'password': '123456'
        })
        api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        api_test_case.assertEqual(response.json(), {'success': True, 'message': 'Create User successfully'})
        response = basic_client.post('/api/login/', {
            'username': 'andrew',
            'password': '123456'
        })
        api_test_case.assertEqual(response.json(), {'success': True})

        # get csrf token
        response = basic_client.get('/api/csrf-token/')
        csrf_token = response.json().get('csrfToken')
        #
        response = basic_client.post('/api/password-change/', {
            'username': 'andrew',
            'password': '1234567'
        }, HTTP_X_CSRFTOKEN=csrf_token, format='json')
        api_test_case.assertEqual(response.json(), {'success': True, 'message': 'Change password successfully'})
        # login again after changing password
        response = basic_client.post('/api/login/', {
            'username': 'andrew',
            'password': '1234567'
        })
        api_test_case.assertEqual(response.json(), {'success': True})

    def test_reset_password(self, api_test_case, basic_client):
        response = basic_client.post('/api/password-reset/', {
            'email': 'test_user@gmail.com'
        })
        response = basic_client.get('/api/password-reset/done/')
        outbox = mail.EmailMessage().body
        print(outbox)

    def test_google_authentication(self, api_test_case, basic_client):
        response = basic_client.post('/social-auth/complete/google-oauth2/')
        print(response.content)