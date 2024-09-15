from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Tenant
from .serializers import TenantSerializer


# Create your views here.
class TenantViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()
