from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractors

class BaseTest(APITestCase):
    client = APIClient()

class CreateContractorsTest(BaseTest):

    def test_it_can_create_a_contractor(self):
        data = {
        'name': 'Builder Bob',
        'email': 'test@mail.com',
        'phone_number': '111111111',
        'zip': '80124',
        'specialty': 'construction',
        'logo': 'logo.jpg'
        }
        response = self.client.post('/api/v1/contracors', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
