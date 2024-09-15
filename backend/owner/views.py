from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Owner
from .serializers import OwnerSerializer


class OwnerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
