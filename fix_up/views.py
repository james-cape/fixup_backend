from rest_framework import generics
import json
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import HttpRequest
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

class ListProjectBatchView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        contractor = Contractor.objects.filter(id=self.request.query_params['contractor_id'])[0]
        projects = Project.objects.filter(category=contractor.category)
        ContractorProject.objects.create(contractor=contractor, project=projects[0])
        ContractorProject.objects.create(contractor=contractor, project=projects[1])
        ContractorProject.objects.create(contractor=contractor, project=projects[2])
        ContractorProject.objects.create(contractor=contractor, project=projects[3])
        ContractorProject.objects.create(contractor=contractor, project=projects[4])
        ContractorProject.objects.create(contractor=contractor, project=projects[5])
        ContractorProject.objects.create(contractor=contractor, project=projects[6])
        ContractorProject.objects.create(contractor=contractor, project=projects[7])
        ContractorProject.objects.create(contractor=contractor, project=projects[8])
        ContractorProject.objects.create(contractor=contractor, project=projects[9])

        return projects
