import typing as tp
from django.db.models.base import ModelState


class RequestMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


def filter_query(query: tp.Union[list, dict]) -> tp.Union[list, dict]:
    if isinstance(query, dict):
        return {k: v for k, v in query.items() if not isinstance(v, ModelState)}
    return [{k: v for k, v in q.items() if not isinstance(v, ModelState)} for q in query]
