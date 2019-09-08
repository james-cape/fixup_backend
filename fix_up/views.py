from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contractor
from .models import Project
from .models import ContractorProject
from .serializers import ContractorSerializer
from .serializers import ProjectSerializer
from .serializers import ContractorProjectSerializer
from .serializers import ProjectSerializerForUsers
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer

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
# Gets a list of projects (with contractors)
class ListProjectsByUser(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, **kwargs):
        queryset = []
        user_projects = Project.objects.filter(user=self.kwargs["user_id"])
        for user_project in user_projects:
            contractor_projects = user_project.contractorproject_set.all()
            contractor_accumulator = []
            for contractor_project in contractor_projects:
                contractor_accumulator.append({
                    'contractor_id': contractor_project.contractor.id,
                    'picture_1': contractor_project.contractor.example_project_1,
                    'picture_2': contractor_project.contractor.example_project_2
                })
            queryset.append({
                'id': user_project.id,
                'title': user_project.title,
                'description': user_project.description,
                'category': user_project.category,
                'user_before_picture': user_project.user_before_picture,
                'user_after_picture': user_project.user_after_picture,
                'contractors': contractor_accumulator
            })
        return Response(queryset)
