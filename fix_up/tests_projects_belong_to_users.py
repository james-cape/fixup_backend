from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractor
from .models import ContractorProject
from .models import Project
from .models import User
from .serializers import Contractorerializer

class BaseTest(APITestCase):
    client = APIClient()

class CreateContractorProjectTest(BaseTest):

    def test_it_can_create_a_contractor_project_join_table(self):

        contractor_1 = Contractor(
            id=1,
            name='Mario',
            email='test@mail.com',
            phone_number='111111111',
            zip='80124',
            category='plumbing',
            logo='logo.jpg'
        )
        contractor_1.save()

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
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_1.save()

        project_2 = Project(
            id=2,
            user=user_1,
            title='project_numero_dos',
            description='this is the second project',
            category='plumbing',
            user_before_picture='picture.png',
            user_after_picture='picture.png'
        )
        project_2.save()

        self.assertEqual(project_1.user, user_1)
        self.assertEqual(project_2.user, user_1)
        self.assertEqual(user_1.project_set.all()[1].title, 'project_numero_uno')
        self.assertEqual(user_1.project_set.all()[0].title, 'project_numero_dos')
