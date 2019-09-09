from rest_framework import serializers
from .models import User
from .models import Contractor
from .models import Project
from .models import ContractorProject

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone_number', 'zip')

class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ('name', 'email', 'phone_number', 'zip', 'category', 'logo')

class ContractorProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorProject
        fields = ('project', 'contractor', 'contractor_choice', 'user_choice', 'seen', 'completed', 'contractor_before_picture', 'contractor_after_picture', 'user_rating', 'contractor_rating')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'category', 'user_before_picture', 'user_after_picture')

class ProjectSerializerForUsers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'category', 'user_before_picture', 'user_after_picture', 'contractors']
