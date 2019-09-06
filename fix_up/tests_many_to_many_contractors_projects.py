from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractor
from .models import ContractorProject
from .models import Project
from .models import User
from .serializers import ContractorSerializer

class BaseTest(APITestCase):
    client = APIClient()

class CreateContractorProjectTest(BaseTest):

    def test_it_can_create_a_contractor_project_join_table(self):

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

        contractor_project_1 = ContractorProject(
            project=project_1,
            contractor=contractor_1,
            contractor_choice=0,
            user_choice=False,
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
            user_choice=False,
            seen=False,
            completed=False,
            contractor_before_picture='picture.png',
            contractor_after_picture='picture.png',
            user_rating=5,
            contractor_rating=5
        )
        contractor_project_3.save()

        contractor_project_4 = ContractorProject(
            project=project_2,
            contractor=contractor_2,
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

        self.assertEqual(contractor_1.contractorproject_set.all()[0].project.title, project_2.title)
        self.assertEqual(contractor_1.contractorproject_set.all()[1].project.title, project_1.title)
        self.assertEqual(contractor_2.contractorproject_set.all()[0].project.title, project_2.title)
        self.assertEqual(contractor_2.contractorproject_set.all()[1].project.title, project_1.title)
