import urllib3

BASE_URL = "https://stats.data.gouv.fr/index.php?"
API_ACTION = "apiAction=get&apiModule=API"
TOKEN = "&token_auth=anonymous"
FORMAT_METRICS = "&format_metrics=1"
FORMAT = "&format=JSON"
MODULE = "&module=API"
EXPANDED = "&expanded=1"
FILTER_LIMIT = "&filter_limit=-1"
ID_SITE = "&idSite=150"
PERIOD = "&period=week"

FULL_REPORT = "&method=API.getProcessedReport"
RAW_REPORT = "&method=API.get"


def init():
    global http
    http = urllib3.PoolManager()
