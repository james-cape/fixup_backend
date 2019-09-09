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

class ShowUserTest(BaseTest):

    def test_it_can_return_user_data(self):

        user_1 = User(
            full_name='Princess',
            email='this_castle@mail.com',
            phone_number='44336',
            zip='13335'
        )
        user_1.save()

        user_2 = User(
            full_name='other_Princess',
            email='another_castle@mail.com',
            phone_number='1234566',
            zip='12345'
        )
        user_2.save()

        response = self.client.get(f'/api/v1/users/{user_1.id}', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], user_1.full_name)
        self.assertEqual(response.data['full_name'], user_1.full_name)
        self.assertEqual(response.data['email'], user_1.email)
        self.assertEqual(response.data['phone_number'], user_1.phone_number)
        self.assertEqual(response.data['zip'], user_1.zip)
