from rest_framework import serializers
from .models import Contractor

class Contractorerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ('name', 'email', 'phone_number', 'zip', 'category', 'logo')
