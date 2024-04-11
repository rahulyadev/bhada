
from .models import Tenant, User

from bhada.serializers import ValidateModelSerializer
from account.serializers import UserDetailReadOnlySerializer

from .models import Tenant
class TenantSerializer(ValidateModelSerializer):
    """Tenant Serializer"""

    NESTED_FIELDS_TO_QUERYSET = {
        "user" : User.objects.all(),
    }
    user = UserDetailReadOnlySerializer(required=False)
    class Meta:
        model = Tenant
        fields = ['id', 'user', 'aadhar_card_number', 'pan_card_number', 'dob', 'education']
        read_only_fields = ["id"]
