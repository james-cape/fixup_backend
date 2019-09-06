# from rest_framework.test import APITestCase, APIClient, APIRequestFactory
# from rest_framework.views import status
# from .models import Contractor
# from .serializers import ContractorSerializer
#
# class BaseTest(APITestCase):
#     client = APIClient()
#
# class ProjectCrudTest(BaseTest):
#
#     def test_it_can_show_a_project(self):
#
#         user_1 = User(
#             full_name='Princess',
#             email='another_castle@mail.com',
#             phone_number='1234566',
#             zip='12345'
#         )
#         user_1.save()
#
#         project_1 = Project(
#             user=user_1,
#             title='project_numero_uno',
#             description='this is the first project',
#             category='plumbing',
#             user_before_picture='picture.png',
#             user_after_picture='picture.png'
#         )
#         project_1.save()
#
#         project_2 = Project(
#             user=user_1,
#             title='project_numero_dos',
#             description='this is the second project',
#             category='plumbing',
#             user_before_picture='picture.png',
#             user_after_picture='picture.png'
#         )
#         project_2.save()
#
#         response = self.client.get(f'/api/v1/projects/{Project.objects.all()[0].id}', data, format='json')
#
#         self.assertEqual(response.status_code, status.HTTP_200_FOUND)
#         self.assertEqual(response.data['name'], 'Builder Bob')
#         self.assertEqual(response.data['email'], 'test@mail.com')
#         self.assertEqual(response.data['phone_number'], '111111111')
#         self.assertEqual(response.data['zip'], '80124')
#         self.assertEqual(response.data['category'], 'construction')
#         self.assertEqual(response.data['logo'], 'logo.jpg')
#
# # class UpdateContractorTest(BaseTest):
# #     def test_it_can_update_a_contractor(self):
# #         data = {
# #         'name': 'user_1',
# #         'email': 'user_1@mail.com',
# #         'phone_number': '111111111',
# #         'zip': '80124',
# #         'category': 'construction',
# #         'logo': 'logo.jpg'
# #         }
# #         response = self.client.post('/api/v1/Contractor/', data, format='json')
# #         self.assertEqual(Contractor.objects.all()[0].name, 'user_1')
# #         self.assertEqual(Contractor.objects.all()[0].email, 'user_1@mail.com')
# #
# #         # Tests changing just the name
# #         update_data = {
# #         'name': 'new_name_1'
# #         }
# #         update_response_1 = self.client.patch(f'/api/v1/Contractor/{Contractor.objects.all()[0].id}', update_data, format='json')
# #         self.assertEqual(Contractor.objects.all()[0].name, 'new_name_1')
# #         self.assertEqual(Contractor.objects.all()[0].email, 'user_1@mail.com')
# #         self.assertEqual(update_response_1.status_code, 200)
# #
# #         # Tests changing just the name again as well as the email
# #         update_data = {
# #         'name': 'new_name_2',
# #         'email': 'new_user_1@mail.com'
# #         }
# #         update_response_1 = self.client.patch(f'/api/v1/Contractor/{Contractor.objects.all()[0].id}', update_data, format='json')
# #         self.assertEqual(Contractor.objects.all()[0].name, 'new_name_2')
# #         self.assertEqual(Contractor.objects.all()[0].email, 'new_user_1@mail.com')
# #         self.assertEqual(update_response_1.status_code, 200)
