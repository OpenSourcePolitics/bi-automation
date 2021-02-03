from settings import * # noqa
from http_handler import http_get
from date import get_report_dates
from pprint import pprint

from datetime import date, timedelta


def main():
    init()  # noqa
    report = get_weekly_report()
    pprint(report)
    pprint(get_week_total_visits(report))
    pprint(get_avg_visit_time(report))
    pprint(get_bounce_rate(report))


def get_weekly_report():
    global DATE
    DATE = get_report_dates(date.today()-timedelta(7))
    http_request = set_uri()
    return http_get(http_request)


def set_uri():
    return f"""{BASE_URL}{API_ACTION}{TOKEN}{FORMAT_METRICS}{FORMAT}{MODULE}{EXPANDED}{FILTER_LIMIT}{ID_SITE}{DATE}{PERIOD}{FULL_REPORT}"""


def get_week_total_visits(report):
    return report['reportTotal']['nb_visits']


def get_avg_visit_time(report):
    metadata = get_metadata(report)
    return metadata['avg_time_on_site']


def get_bounce_rate(report):
    metadata = get_metadata(report)
    return metadata['bounce_rate']


def get_metadata(report):
    week_key = list(report['reportData'].keys())[0]
    return report['reportData'][week_key]


main()
