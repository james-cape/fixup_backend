from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import User
from .serializers import UserSerializer

class BaseTest(APITestCase):
    client = APIClient()

class CreateUserTest(BaseTest):

    def test_it_can_create_a_user(self):
        data = {
            'full_name': 'user_1_name',
            'email': 'user_1_email@email.com',
            'phone_number': '3333333',
            'zip': '98765'
        }
        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], 'user_1_name')
        self.assertEqual(response.data['email'], 'user_1_email@email.com')
        self.assertEqual(response.data['phone_number'], '3333333')
        self.assertEqual(response.data['zip'], '98765')
