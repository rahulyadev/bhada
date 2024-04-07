from account.models import User
from account.serializers import UserDetailReadOnlySerializer
from bhada.serializers import ValidateModelSerializer

from .models import Owner


class OwnerSerializer(ValidateModelSerializer):
    """Owner Serializer."""

    NESTED_FIELDS_TO_QUERYSET = {
        "user": User.objects.all(),
    }
    user = UserDetailReadOnlySerializer(required=False)

    class Meta:
        model = Owner
        fields = ["id", "user", "upi_id"]
        read_only_fields = ["id"]
