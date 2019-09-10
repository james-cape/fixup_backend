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
        self.assertEqual(update_response_1.status_code, 204)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].user_choice, True)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].user_choice, False)
        self.assertEqual(update_response_1.data['message'], "You've been Fixed Up!")
        self.assertEqual(update_response_1.data['contractor'], {
            "name": contractor_1.name,
            "email": contractor_1.email,
            "phone_number": contractor_1.phone_number,
            "zip": contractor_1.zip,
            "category": contractor_1.category,
            "logo": contractor_1.logo
        })
        self.assertEqual(update_response_1.data['project'], {
            "title": project_1.title,
            "description": project_1.description,
            "category": project_1.category,
            "user_before_picture": project_1.user_before_picture,
            "user_after_picture": project_1.user_after_picture
        })
        self.assertEqual(update_response_1.data['user'], {
            "full_name": user.full_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "zip": user.zip
        })

        #### WARIO
        #### Tests updating contractor_project_2.user_choice to TRUE
        update_response_2 = self.client.patch(f'/api/v1/projects/{Project.objects.all()[0].id}/contractors/{contractor_2.id}?user_choice=True', format='json')
        self.assertEqual(update_response_2.status_code, 204)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].user_choice, True)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].user_choice, True)
        self.assertEqual(update_response_2.data['message'], "You've been Fixed Up!")
        self.assertEqual(update_response_2.data['contractor'], {
            "name": contractor_2.name,
            "email": contractor_2.email,
            "phone_number": contractor_2.phone_number,
            "zip": contractor_2.zip,
            "category": contractor_2.category,
            "logo": contractor_2.logo
        })
        self.assertEqual(update_response_2.data['project'], {
            "title": project_1.title,
            "description": project_1.description,
            "category": project_1.category,
            "user_before_picture": project_1.user_before_picture,
            "user_after_picture": project_1.user_after_picture
        })
        self.assertEqual(update_response_2.data['user'], {
            "full_name": user.full_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "zip": user.zip
        })

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
        swipe_left = {
            "contractor_choice": 1
        }
        update_response_1 = self.client.patch(f'/api/v1/contractors/{contractor_1.id}/projects/{Project.objects.all()[0].id}', swipe_left, format='json')
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].contractor_choice, 1)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].contractor_choice, 0)
        self.assertEqual(update_response_1.data['message'], 'contractor_project contractor_choice updated to 1')
        self.assertEqual(update_response_1.status_code, 204)

        #### WARIO
        #### Tests updating contractor_project_2.contractor_choice to 2 (RIGHT swipe)
        swipe_right = {
        "contractor_choice": 2
        }
        update_response_2 = self.client.patch(f'/api/v1/contractors/{contractor_2.id}/projects/{Project.objects.all()[0].id}', swipe_right, format='json')
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_1.id)[0].contractor_choice, 1)
        self.assertEqual(ContractorProject.objects.filter(contractor_id=contractor_2.id)[0].contractor_choice, 2)
        self.assertEqual(update_response_2.data['message'], 'contractor_project contractor_choice updated to 2')
        self.assertEqual(update_response_2.status_code, 204)
