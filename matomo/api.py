import settings as settings
import requests as requests
from datetime import date, timedelta
from pprint import pprint

BASE_URL = "https://stats.data.gouv.fr/index.php?"
API_ACTION = "apiAction=get&apiModule=API"
TOKEN = "&token_auth=anonymous"
FORMAT_METRICS = "&format_metrics=1"
FORMAT = "&format=JSON"
MODULE = "&module=API"
EXPANDED = "&expanded=1"
FILTER_LIMIT = "&filter_limit=-1"
ID_SITE = "&idSite=150"
PERIOD = "&period=day"

FULL_REPORT = "&method=API.getProcessedReport"
RAW_REPORT = "&method=API.get"


def main():
    settings.init()
    report = get_weekly_report()
    pprint(get_week_total_visits(report))


def get_weekly_report():
    global DATE
    DATE = get_report_dates()
    request = set_uri()
    return requests.get(request)


def set_uri():
    return f"{BASE_URL}{API_ACTION}{TOKEN}{FORMAT_METRICS}{FORMAT}{MODULE}{EXPANDED}{FILTER_LIMIT}{ID_SITE}{DATE}{PERIOD}{FULL_REPORT}"  # noqa


def get_week_total_visits(report):
    return report['reportTotal']['nb_visits']


def get_report_dates():
    now = date.today()
    start_date = now - timedelta(now.weekday())
    end_date = start_date + timedelta(6)
    return f"""
        &date={start_date.strftime('%Y-%m-%d')},{end_date.strftime('%Y-%m-%d')}
    """


main()
