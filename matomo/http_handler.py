import json
import settings


def http_get(uri):
    r = settings.http.request("GET", uri)
    return json.loads(r.data.decode('utf-8'))
