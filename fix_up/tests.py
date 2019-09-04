from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractors
from .serializers import ContractorSerializer

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
        response = self.client.post('/api/v1/contracors/', data, format='json')

        # import code; code.interact(local=dict(globals(), **locals()))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Builder Bob')
        self.assertEqual(response.data['email'], 'test@mail.com')
        self.assertEqual(response.data['phone_number'], '111111111')
        self.assertEqual(response.data['zip'], '80124')
        self.assertEqual(response.data['specialty'], 'construction')
        self.assertEqual(response.data['logo'], 'logo.jpg')
