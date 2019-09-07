from rest_framework import generics
from .models import Contractor
from .models import Project
from .serializers import ContractorSerializer
from .serializers import ProjectSerializer

#### Contractors
class CreateContractorView(generics.CreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class SingleContractorView(generics.UpdateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

#### Projects
class SingleProjectView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class IndexProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
