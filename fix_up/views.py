from rest_framework import generics
from .models import Contractor
from .models import Project
from .models import ContractorProject
from .serializers import ContractorSerializer
from .serializers import ProjectSerializer
from .serializers import ContractorProjectSerializer

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

class ListProjectsByContractor(generics.ListAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        filtered = ContractorProject.objects.filter(contractor=self.kwargs["contractor_id"])
        return [element.project for element in filtered]
