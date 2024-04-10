from rest_framework import serializers
from .models import Tenant
from account.serializers import UserDetailsSerializer

class TenantSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    class Meta:
        model = Tenant
        fields = ['id', 'user', 'aadhar_card_number', 'pan_card_number', 'dob', 'education']
