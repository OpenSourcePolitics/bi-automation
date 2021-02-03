from settings import * # noqa
from http_handler import http_get
from date import get_report_dates
from pprint import pprint


def main():
    init()  # noqa
    report = get_weekly_report()
    pprint(get_week_total_visits(report))


def get_weekly_report():
    global DATE
    DATE = get_report_dates()
    request = set_uri()
    return http_get(request)


def set_uri():
    return f"{BASE_URL}{API_ACTION}{TOKEN}{FORMAT_METRICS}{FORMAT}{MODULE}{EXPANDED}{FILTER_LIMIT}{ID_SITE}{DATE}{PERIOD}{FULL_REPORT}"  # noqa


def get_week_total_visits(report):
    return report['reportTotal']['nb_visits']


main()
