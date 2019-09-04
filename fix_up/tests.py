from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Contractors
from .serializers import ContractorSerializer



class GetAllContractorsTest(APITestCase):
    def setUp(self):



    def test_it_can_get_contractors:
