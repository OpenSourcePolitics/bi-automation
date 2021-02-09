import settings


def http_get(request, params=None):
    response_status, response_content = settings.metabase.get(request, params)
    assert response_status
    return response_content


def http_post(request, json=None):
    response_status, response_content = settings.metabase.post(request, json)
    assert response_status
    return response_content
