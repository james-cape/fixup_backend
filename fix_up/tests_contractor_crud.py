from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractor
from .serializers import ContractorSerializer

class BaseTest(APITestCase):
    client = APIClient()

class CreateContractorTest(BaseTest):

    def test_it_can_create_a_contractor(self):
        data = {
        'name': 'Builder Bob',
        'email': 'test@mail.com',
        'phone_number': '111111111',
        'zip': '80124',
        'category': 'construction',
        'logo': 'logo.jpg'
        }
        response = self.client.post('/api/v1/contractors/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Builder Bob')
        self.assertEqual(response.data['email'], 'test@mail.com')
        self.assertEqual(response.data['phone_number'], '111111111')
        self.assertEqual(response.data['zip'], '80124')
        self.assertEqual(response.data['category'], 'construction')
        self.assertEqual(response.data['logo'], 'logo.jpg')

class UpdateContractorTest(BaseTest):
    def test_it_can_update_a_contractor(self):
        data = {
        'name': 'user_1',
        'email': 'user_1@mail.com',
        'phone_number': '111111111',
        'zip': '80124',
        'category': 'construction',
        'logo': 'logo.jpg'
        }
        response = self.client.post('/api/v1/contractors/', data, format='json')
        self.assertEqual(Contractor.objects.all()[0].name, 'user_1')
        self.assertEqual(Contractor.objects.all()[0].email, 'user_1@mail.com')

        # Tests changing just the name
        update_data = {
        'name': 'new_name_1'
        }
        update_response_1 = self.client.patch(f'/api/v1/contractors/{Contractor.objects.all()[0].id}', update_data, format='json')
        self.assertEqual(Contractor.objects.all()[0].name, 'new_name_1')
        self.assertEqual(Contractor.objects.all()[0].email, 'user_1@mail.com')
        self.assertEqual(update_response_1.status_code, 200)

        # Tests changing just the name again as well as the email
        update_data = {
        'name': 'new_name_2',
        'email': 'new_user_1@mail.com'
        }
        update_response_1 = self.client.patch(f'/api/v1/contractors/{Contractor.objects.all()[0].id}', update_data, format='json')
        self.assertEqual(Contractor.objects.all()[0].name, 'new_name_2')
        self.assertEqual(Contractor.objects.all()[0].email, 'new_user_1@mail.com')
        self.assertEqual(update_response_1.status_code, 200)
