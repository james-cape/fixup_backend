from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractor
from .models import User
from .models import Project
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
