from rest_framework import generics
from .models import Contractor
from .serializers import Contractorerializer

class CreateContractorView(generics.CreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = Contractorerializer

class SingleContractorView(generics.UpdateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = Contractorerializer
