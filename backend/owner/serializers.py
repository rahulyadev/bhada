from rest_framework import serializers
from .models import Owner
from account.serializers import UserDetailsSerializer


class OwnerSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(required=False, read_only=True)

    class Meta:
        model = Owner
        fields = ['id', 'user', 'upi_id']
        
