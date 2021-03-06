from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractor
from .models import User
from .models import Project
from .models import ContractorProject
from .serializers import ContractorSerializer
from .serializers import ProjectSerializer

class BaseTest(APITestCase):
    client = APIClient()

class UserSeesTheirProjectsTest(BaseTest):

    def test_getting_all_of_a_users_projects(self):

        user_1 = User(
            full_name='Princess',
            email='another_castle@mail.com',
            phone_number='1234566',
            zip='12345'
        )
        user_1.save()

        user_2 = User(
            full_name='Bowser',
            email='my_castle@mail.com',
            phone_number='2234566',
            zip='22345'
        )
        user_2.save()

        project_1 = Project(
            user=user_1,
            title='project_numero_uno',
            description='this is the first project',
            category='plumbing',
            user_before_picture='picture.png'
        )
        project_1.save()

        project_2 = Project(
            user=user_1,
            title='project_numero_dos',
            description='this is the second project',
            category='plumbing',
            user_before_picture='picture.png'
        )
        project_2.save()

        project_3 = Project(
            user=user_2,
            title='project_numero_tres',
            description='this is the third project',
            category='plumbing',
            user_before_picture='picture.png'
        )
        project_3.save()

        contractor_1 = Contractor(
            name='Mario',
            email='mario@mail.com',
            phone_number='111111111',
            zip='80124',
            category='plumbing',
            logo='logo.jpg',
            example_project_1='picture.png',
            example_project_2='picture.png'
        )
        contractor_1.save()

        contractor_2 = Contractor(
            name='Luigi',
            email='Luigi@mail.com',
            phone_number='222222222',
            zip='80224',
            category='plumbing',
            logo='logo.jpg',
            example_project_1='picture.png',
            example_project_2='picture.png'
        )
        contractor_2.save()

        contractor_project_1 = ContractorProject(
            project=project_2,
            contractor=contractor_1,
            contractor_choice=0,
            user_choice=True,
            completed=False,
            seen=False,
            contractor_before_picture='picture.png',
            user_rating=5,
            contractor_rating=5
        )
        contractor_project_1.save()

        contractor_project_2 = ContractorProject(
            project=project_2,
            contractor=contractor_2,
            contractor_choice=2,
            user_choice=True,
            completed=False,
            seen=False,
            contractor_before_picture='picture.png',
            user_rating=5,
            contractor_rating=5
        )
        contractor_project_2.save()

        response = self.client.get(f'/api/v1/users/{user_1.id}/projects', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['id'], project_2.id)
        self.assertEqual(response.data[0]['title'], project_2.title)
        self.assertEqual(response.data[0]['description'], project_2.description)
        self.assertEqual(response.data[0]['category'], project_2.category)
        self.assertEqual(response.data[0]['user_before_picture'], project_2.user_before_picture)
        self.assertEqual(response.data[0]['user_after_picture'], project_2.user_after_picture)
        self.assertEqual(response.data[0]['contractors'][0], {
            'contractor_id': contractor_2.id,
            'picture_1': contractor_2.example_project_1,
            'picture_2': contractor_2.example_project_2,
            'user_choice': True
        })
