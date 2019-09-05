from rest_framework import generics
from .models import Contractors
from .serializers import ContractorSerializer

class CreateContractorView(generics.CreateAPIView):
    queryset = Contractors.objects.all()
    serializer_class = ContractorSerializer

class SingleContractorView(generics.UpdateAPIView):
    queryset = Contractors.objects.all()
    serializer_class = ContractorSerializer
