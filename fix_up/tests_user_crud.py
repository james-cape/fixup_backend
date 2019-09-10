from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import User
from .models import Project
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

class GetUserTest(BaseTest):

    def test_it_can_get_a_user_and_their_projects(self):
        user = User(
            id=1,
            full_name='User Userton',
            email='user@mail.com',
            phone_number='1234567890',
            zip='80555'
        )

        user.save()

        project_1 = Project(
            id=1,
            user=user,
            title='project_numero_uno',
            description='this is the first project',
            category='plumbing',
            user_before_picture='picture.png'
        )
        project_1.save()

        project_2 = Project(
            id=2,
            user=user,
            title='project_numero_dos',
            description='this is the second project',
            category='plumbing',
            user_before_picture='picture.png'
        )
        project_2.save()

        response = self.client.get('/api/v1/users/1/projects/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['user_id'], 1)
        self.assertEqual(response['project']['id'], 1)
        self.assertEqual(response['project']['title'], 'project_numero_uno')
        self.assertEqual(response['project']['description'], 'this is the first project')

        response_2 = self.client.get('/api/v1/users/1/projects/2/')

        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_2['user_id'], 1)
        self.assertEqual(response_2['project']['id'], 2)
        self.assertEqual(response_2['project']['title'], 'project_numero_dos')
        self.assertEqual(response_2['project']['description'], 'this is the second project')
