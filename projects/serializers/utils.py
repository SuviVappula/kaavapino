from collections import namedtuple

from django.contrib.auth import get_user_model
from rest_framework import serializers

from projects.models import Attribute

FIELD_TYPES = {
    Attribute.TYPE_SHORT_STRING: serializers.CharField,
    Attribute.TYPE_LONG_STRING: serializers.CharField,
    Attribute.TYPE_INTEGER: serializers.IntegerField,
    Attribute.TYPE_BOOLEAN: serializers.BooleanField,
    Attribute.TYPE_DATE: serializers.DateField,
    Attribute.TYPE_IMAGE: serializers.ImageField,
    Attribute.TYPE_FILE: serializers.FileField,
    Attribute.TYPE_USER: serializers.PrimaryKeyRelatedField,
    # TODO Add Attribute.TYPE_GEOMETRY
}

FieldData = namedtuple("FieldData", ["field_class", "field_arguments"])


def _get_serializer_field_data(attribute):
    field_arguments = {}
    field_class = FIELD_TYPES.get(attribute.value_type, None)

    choices = attribute.value_choices.all()
    if choices:
        field_class = serializers.SlugRelatedField
        field_arguments["queryset"] = choices
        field_arguments["slug_field"] = "identifier"

        if attribute.multiple_choice:
            field_arguments["many"] = True

    if attribute.value_type == Attribute.TYPE_USER:
        field_class = serializers.SlugRelatedField
        field_arguments["queryset"] = get_user_model().objects.all()
        field_arguments["slug_field"] = "uuid"

    field_arguments["help_text"] = attribute.help_text

    # Allow fields to be set to null so that they can be emptied
    if attribute.value_type not in [Attribute.TYPE_BOOLEAN]:
        field_arguments["allow_null"] = True

    return FieldData(field_class, field_arguments)


def _is_attribute_required(section_attribute):
    attribute = section_attribute.attribute

    if (
        attribute.value_type != Attribute.TYPE_BOOLEAN
        and not section_attribute.generated
    ):
        return section_attribute.required
    else:
        return False
