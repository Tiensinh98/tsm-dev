from django.db import models

from .. import utils

__all__ = ['ConverterMixin']

class ConverterMixin:

    @classmethod
    def from_json_value(cls, json_value: dict):
        arguments = {}
        field_to_converter = cls.get_non_primitive_field_to_converter()
        for key, value in json_value.items():
            if key in cls.__dict__.keys():
                if key in field_to_converter:
                    value = field_to_converter[key](value)
                arguments[key] = value
        return cls(**arguments)

    @classmethod
    def get_non_primitive_field_to_converter(cls) -> dict:
        d = {}
        if cls.__base__ == models.Model:
            field_key_pairs = cls.__dict__
        elif cls.__base__.__base__ == models.Model:
            field_key_pairs = {**cls.__dict__, **cls.__base__.__dict__}
        else:
            assert False
        for field_name, field_obj in field_key_pairs.items():
            if not isinstance(field_obj, (
                    models.fields.related_descriptors.ForwardManyToOneDescriptor,
                    models.query_utils.DeferredAttribute
            )):
                continue
            if '_ptr' in field_name or '_id' in field_name:
                continue
            field = getattr(field_obj, 'field', None)
            if field is None:
                continue
            if isinstance(field, models.DateField):
                d[field_name] = utils.get_datetime_from_str
            elif isinstance(field, models.CharField):
                if field.choices is not None:
                    # TODO: convert field_name to GUI name for front end
                    pass
            elif isinstance(field, (models.ForeignKey, models.OneToOneField)):
                d[f'{field_name}_id'] = lambda _id: (field.model.objects.get(id=_id), field_name)
        return d


class JsonResponseMixin:
    @classmethod
    def get_json_value(cls):
        return


class JsonRequestMixin:
    @classmethod
    def from_json_value(cls, json_value: dict):
        arguments = {}
        field_to_converter = cls.get_non_primitive_field_to_converter()
        for key, value in json_value.items():
            if key in cls.__dict__.keys():
                if key in field_to_converter:
                    value = field_to_converter[key](value)
                arguments[key] = value
        return cls(**arguments)
