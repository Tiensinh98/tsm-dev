import typing as tp
from django.db import models
from django.db.models.base import ModelState


class RequestMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'

