from typing import Any, Dict, List

from django.db import transaction
from django.db.models.base import ModelBase


def convert_validated_nested_field_to_object(
    validated_data,
    nested_field_name,
    queryset,
    partial: bool=False,
    many_to_many: bool=False,
):
    if partial and nested_field_name not in validated_data:
        return validated_data
    if many_to_many:
        validated_data[nested_field_name] = queryset.filter(
            id__in=[
                data["id"] for data in validated_data.pop(nested_field_name, [])
            ]
        )
    else:
        nested_field = validated_data.pop(nested_field_name, None)
        validated_data[nested_field_name] = (
            queryset.get(id=nested_field["id"]) if nested_field else None
        )
    return validated_data


def patch_object(obj, dict_obj):
    for k, v in dict_obj.items():
        setattr(obj, k, v)
    return obj


# a helper method that helps create and update related objects for a given object.
@transaction.atomic
def save_related_objects(
    model_class: ModelBase,
    dataset: List[Dict[str, Any]],
    related_kwargs: Dict[str, Any],
    defaults: dict = None,
    create_enabled=True,
    delete_enabled=True,
):
    existing_item_id_to_data = {
        data["id"]: data for data in dataset if data.get("id")
    }
    defaults = defaults or {}

    if delete_enabled:
        # Step 1: Delete all ids which are not provided
        model_class.objects.filter(**related_kwargs).exclude(
            id__in=existing_item_id_to_data.keys()
        ).delete()

    # Step 2: Update existing objects
    updated_objects = []
    for obj in model_class.objects.filter(**related_kwargs).filter(
        id__in=existing_item_id_to_data.keys()
    ):
        patch_object(obj, existing_item_id_to_data[obj.id])
        obj.save()
        updated_objects.append(obj)

    created_objects = []
    if create_enabled:
        # Step 3: Create New Objects
        created_objects = [
            model_class.objects.create(**data, **related_kwargs, **defaults)
            for data in dataset
            if not data.get("id", None)
        ]

    return created_objects + updated_objects
