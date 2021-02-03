import urllib3

BASE_URL = "https://stats.data.gouv.fr/index.php?"
API_ACTION = "get"
API_MODULE = "API"
DATE = ""
EXPANDED = 1
FILTER_LIMIT = "-1"
FLAT = ""
FORMAT = "JSON"
FORMAT_METRICS = 1
ID_SITE = "150"
METHOD = "API.getProcessedReport"
MODULE = "API"
PERIOD = "week"
TOKEN = "anonymous"


# API_ACTION_PAGES_REPORT = "apiAction=getPageUrls&apiModule=Actions"

# val  = "&flat=1&period=range"


def init():
    global http
    http = urllib3.PoolManager()
