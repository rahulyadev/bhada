from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import TenantSerializer
from .models import Tenant

# Create your views here.
class TenantViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()