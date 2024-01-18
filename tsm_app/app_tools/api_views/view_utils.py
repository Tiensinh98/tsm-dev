class RequestMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


def get_related_query_params(query_params: dict, related_name: str):
    if query_params is None:
        query_params = {}
    else:
        query_params = {f'{related_name}__{k}': v for k, v in query_params.items()}
    return query_params