from rest_framework.viewsets import ModelViewSet
from .models import Owner
from .serializers import OwnerSerializer
from rest_framework.permissions import IsAuthenticated


class OwnerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()