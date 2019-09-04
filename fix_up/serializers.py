from rest_framework import serializers
from .models import Contractors

class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractors
        fields = ('name', 'email', 'phone_number', 'zip', 'specialty', 'logo')
