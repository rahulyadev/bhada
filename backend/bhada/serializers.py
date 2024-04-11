from rest_framework import serializers

from bhada.utils import convert_validated_nested_field_to_object


class ValidateModelSerializer(serializers.ModelSerializer):
    NESTED_FIELDS_TO_QUERYSET = {}
    MANY_TO_MANY_NESTED_FIELD_TO_QUERYSET = {}

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        for nested_field, queryset in self.NESTED_FIELDS_TO_QUERYSET.items():
            validated_data = convert_validated_nested_field_to_object(
                validated_data, nested_field, queryset, partial=self.partial
            )
        for (
            nested_many_to_many_field,
            queryset,
        ) in self.MANY_TO_MANY_NESTED_FIELD_TO_QUERYSET.items():
            validated_data = convert_validated_nested_field_to_object(
                validated_data,
                nested_many_to_many_field,
                queryset,
                partial=self.partial,
                many_to_many=True,
            )
        return validated_data
