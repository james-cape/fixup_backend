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

# Ideally we would access query_params for user_choice, but I hard-coded it for now
class ListProjectsByContractor(generics.ListAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        contractor_filtered = ContractorProject.objects.filter(contractor=self.kwargs["contractor_id"])
        user_choice_filtered = contractor_filtered.filter(user_choice=True)
        return [element.project for element in user_choice_filtered]

#### Users
class ListProjectsByUser(generics.ListAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        return Project.objects.filter(user=self.kwargs["user_id"])
