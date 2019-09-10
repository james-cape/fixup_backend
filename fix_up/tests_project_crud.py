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

class ProjectCrudTest(BaseTest):

    def test_it_can_show_a_project(self):

        user_1 = User(
            full_name='Princess',
            email='another_castle@mail.com',
            phone_number='1234566',
            zip='12345'
        )
        user_1.save()

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

        response1 = self.client.get(f'/api/v1/projects/{Project.objects.all()[0].id}', format='json')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.data['title'], project_1.title)
        self.assertEqual(response1.data['description'], project_1.description)
        self.assertEqual(response1.data['category'], project_1.category)
        self.assertEqual(response1.data['user_before_picture'], project_1.user_before_picture)
        self.assertEqual(response1.data['user_after_picture'], None)

        response2 = self.client.get(f'/api/v1/projects/{Project.objects.all()[1].id}', format='json')

        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.data['title'], project_2.title)
        self.assertEqual(response2.data['description'], project_2.description)
        self.assertEqual(response2.data['category'], project_2.category)
        self.assertEqual(response2.data['user_before_picture'], project_2.user_before_picture)
        self.assertEqual(response2.data['user_after_picture'], None)

    def test_it_can_get_a_contractors_project_index(self):

        contractor_1 = Contractor(
            id=1,
            name='Mario',
            email='mario@mail.com',
            phone_number='111111111',
            zip='80124',
            category='plumbing',
            logo='logo.jpg'
        )
        contractor_1.save()

        contractor_2 = Contractor(
            id=2,
            name='Luigi',
            email='luigi@mail.com',
            phone_number='222222222',
            zip='80224',
            category='plumbing',
            logo='logo.jpg'
        )
        contractor_2.save()

        user_1 = User(
            id=1,
            full_name='Princess',
            email='another_castle@mail.com',
            phone_number='1234566',
            zip='12345'
        )
        user_1.save()

        project_1 = Project(
            id=1,
            user=user_1,
            title='project_numero_uno',
            description='this is the first project',
            category='plumbing',
            user_before_picture='picture.png'
        )
        project_1.save()

        project_2 = Project(
            id=2,
            user=user_1,
            title='project_numero_dos',
            description='this is the second project',
            category='plumbing',
            user_before_picture='picture.png'
        )
        project_2.save()

        project_3 = Project(
            id=3,
            user=user_1,
            title='project_numero_tres',
            description='this is the third project',
            category='plumbing',
            user_before_picture='picture.png'
        )
        project_3.save()

        contractor_project_1 = ContractorProject(
            project=project_1,
            contractor=contractor_1,
            contractor_choice=0,
            user_choice=True,
            completed=False,
            seen=False,
            contractor_before_picture='picture.png',
            contractor_after_picture='picture.png',
            user_rating=5,
            contractor_rating=5
        )
        contractor_project_1.save()

        contractor_project_2 = ContractorProject(
            project=project_1,
            contractor=contractor_2,
            contractor_choice=0,
            user_choice=False,
            completed=False,
            seen=False,
            contractor_before_picture='picture.png',
            contractor_after_picture='picture.png',
            user_rating=5,
            contractor_rating=5
        )
        contractor_project_2.save()

        contractor_project_3 = ContractorProject(
            project=project_2,
            contractor=contractor_1,
            contractor_choice=0,
            user_choice=True,
            seen=False,
            completed=False,
            contractor_before_picture='picture.png',
            contractor_after_picture='picture.png',
            user_rating=5,
            contractor_rating=5
        )
        contractor_project_3.save()

        contractor_project_4 = ContractorProject(
            project=project_3,
            contractor=contractor_1,
            contractor_choice=0,
            user_choice=False,
            seen=False,
            completed=False,
            contractor_before_picture='picture.png',
            contractor_after_picture='picture.png',
            user_rating=5,
            contractor_rating=5
        )
        contractor_project_4.save()

        response = self.client.get(f'/api/v1/contractors/{contractor_1.id}/projects', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[1]['title'], project_1.title)
        self.assertEqual(response.data[0]['title'], project_2.title)

class CreateProjectTest(BaseTest):

    def test_it_can_create_a_project(self):
        user_1 = User(
            full_name='Princess',
            email='another_castle@mail.com',
            phone_number='1234566',
            zip='12345'
        )
        user_1.save()

        data = {
            'title': 'project_numero_tres',
            'description': 'this is the third project',
            'category': 'plumbing',
            'user_before_picture': 'picture.png'
        }

        response = self.client.post(f'/api/v1/users/{user_1.id}/projects', data, format='json')
#
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['project']['title'], 'project_numero_tres')
        self.assertEqual(response.data['project']['description'], 'this is the third project')
        self.assertEqual(response.data['project']['picture'], 'picture.png')
