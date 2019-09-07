from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractor
from .models import User
from .models import Project
from .models import ContractorProject
from .serializers import ContractorSerializer

class BaseTest(APITestCase):
    client = APIClient()

    def set_up():
        contractor = Contractor(
            name='Mario',
            email='test@mail.com',
            phone_number='111111111',
            zip='80124',
            category='plumbing',
            logo='logo.jpg'
        )
        contractor.save()

        user = User(
            full_name='Princess',
            email='another_castle@mail.com',
            phone_number='1234566',
            zip='12345'
        )
        user.save()

        project_1 = Project(
            user=user,
            title='project_1',
            description='this is the first project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_1.save()

        project_2 = Project(
            user=user,
            title='project_2',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_2.save()

        project_3 = Project(
            user=user,
            title='project_3',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_3.save()

        project_4 = Project(
            user=user,
            title='project_4',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_4.save()

        project_5 = Project(
            user=user,
            title='project_5',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_5.save()

        project_6 = Project(
            user=user,
            title='project_6',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_6.save()

        project_7 = Project(
            user=user,
            title='project_7',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_7.save()

        project_8 = Project(
            user=user,
            title='project_8',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_8.save()

        project_9 = Project(
            user=user,
            title='project_9',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_9.save()

        project_10 = Project(
            user=user,
            title='project_10',
            description='this is a project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_10.save()

class ProjectBatchTest(BaseTest):
    def test_it_sends_ten_projects(self):
        BaseTest.set_up()

        response = self.client.get('/api/v1/projects?contractor_id=1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'project_1')
        self.assertEqual(response.data[0]['description'], 'this is the first project')
        self.assertEqual(ContractorProject.objects.count(), 10)
