import json
import settings


def get(uri):
    r = settings.http.request("GET", uri)
    return json.loads(r.data.decode('utf-8'))
