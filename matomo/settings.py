import urllib3
import yaml

API_ACTION = "get"
API_MODULE = "API"
DATE = ""
EXPANDED = 0
FILTER_LIMIT = "-1"
FLAT = 0
FORMAT = "JSON"
FORMAT_METRICS = 0
METHOD = "API.getProcessedReport"
MODULE = "API"
PERIOD = "range"


def init():
    global http, BASE_URL, ID_SITE, TOKEN
    with open('matomo/secrets.yml', 'r') as f:
        data = yaml.safe_load(f)
        BASE_URL = data['matomo']['base_url'] + "/index.php?"
        ID_SITE = data['matomo']['id_site']
        TOKEN = data['matomo']['token']
    http = urllib3.PoolManager()


def get_pages_urls():
    pages_urls = []
    with open("matomo/requests.yml", "r") as f:
        for page_url in yaml.safe_load(f)['urls']:
            pages_urls.append(f"^{page_url}.*")

    return pages_urls
