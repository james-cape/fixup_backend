from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import User
from .models import Project
from .models import Contractor
from .models import ContractorProject
from .serializers import ContractorSerializer

class BaseTest(APITestCase):
    client = APIClient()

class UserSelectsContractorTest(BaseTest):
    def test_it_updates_user_to_True(self):

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

        contractor_1 = Contractor(
            name='Mario',
            email='test@mail.com',
            phone_number='111111111',
            zip='80124',
            category='plumbing',
            logo='logo.jpg'
        )
        contractor_1.save()

        contractor_2 = Contractor(
            name='Wario',
            email='test@mail.com',
            phone_number='111111111',
            zip='80124',
            category='plumbing',
            logo='logo.jpg'
        )
        contractor_2.save()

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

        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].user_choice, False)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].user_choice, False)

        #### MARIO
        #### Tests updating contractor_project_1.user_choice to TRUE
        update_response_1 = self.client.patch(f'/api/v1/projects/{Project.objects.all()[0].id}/contractors/{contractor_1.id}?user_choice=True', format='json')
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].user_choice, True)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].user_choice, False)
        self.assertEqual(update_response_1.data['message'], 'contractor_project user_choice updated to True')
        self.assertEqual(update_response_1.status_code, 204)

        #### WARIO
        #### Tests updating contractor_project_2.user_choice to TRUE
        update_response_2 = self.client.patch(f'/api/v1/projects/{Project.objects.all()[0].id}/contractors/{contractor_2.id}?user_choice=True', format='json')
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].user_choice, True)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].user_choice, True)
        self.assertEqual(update_response_2.data['message'], 'contractor_project user_choice updated to True')
        self.assertEqual(update_response_2.status_code, 204)

class SwipeUpdateContractorChoiceTest(BaseTest):
    def test_it_updates_contractor_choice_on_swipe(self):

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

        contractor_1 = Contractor(
            name='Mario',
            email='test@mail.com',
            phone_number='111111111',
            zip='80124',
            category='plumbing',
            logo='logo.jpg'
        )
        contractor_1.save()

        contractor_2 = Contractor(
            name='Wario',
            email='test@mail.com',
            phone_number='111111111',
            zip='80124',
            category='plumbing',
            logo='logo.jpg'
        )
        contractor_2.save()

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

        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].contractor_choice, 0)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].contractor_choice, 0)

        #### MARIO
        #### Tests updating contractor_project_1.contractor_choice to 1 (LEFT swipe)
        update_response_1 = self.client.patch(f'/api/v1/contractors/{contractor_1.id}/projects/{Project.objects.all()[0].id}?contractor_choice=1', format='json')
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].contractor_choice, 1)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].contractor_choice, 0)
        self.assertEqual(update_response_1.data['message'], 'contractor_project contractor_choice updated to 1')
        self.assertEqual(update_response_1.status_code, 204)

        #### WARIO
        #### Tests updating contractor_project_2.contractor_choice to 2 (RIGHT swipe)
        update_response_2 = self.client.patch(f'/api/v1/contractors/{contractor_2.id}/projects/{Project.objects.all()[0].id}?contractor_choice=2', format='json')
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].contractor_choice, 1)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].contractor_choice, 2)
        self.assertEqual(update_response_2.data['message'], 'contractor_project contractor_choice updated to 2')
        self.assertEqual(update_response_2.status_code, 204)
