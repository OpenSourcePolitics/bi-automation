import settings # noqa
from http_handler import http_get
from date import get_report_dates
from pprint import pprint

from datetime import date, timedelta


def main():
    settings.init()  # noqa
    global report
    report = get_report()
    pprint(get_week_total_visits())
    pprint(get_avg_visit_time())
    pprint(get_bounce_rate())

    pages_urls = ["/processes/transformation-numerique/f/5/","/processes/transformation-numerique/f/2/"]  # noqa
    get_visited_urls_number_of_visit(pages_urls)


def get_report(type="general"):
    settings.DATE = get_report_dates(date.today()-timedelta(7))
    http_request = set_uri(type)
    return http_get(http_request)


def get_visited_urls_number_of_visit(pages_urls=[]):
    pages_report = get_report("pages")
    report_data = pages_report['reportData']
    for page_url in pages_urls:
        for page in report_data:
            if page['label'] == page_url:
                print(f"{page_url} visited {page['nb_visits']} times")  # noqa


def set_uri(request_type):
    if request_type == "general":
        pass
    elif request_type == "pages":
        settings.API_ACTION = "getPageUrls"
        settings.API_MODULE = "Actions"
        settings.FLAT = "1"
        settings.PERIOD = "range"
        settings.FORMAT_METRICS = 0
        settings.EXPANDED = 0
    uri = (
        settings.BASE_URL +
        f"apiAction={settings.API_ACTION}" +
        f"&apiModule={settings.API_MODULE}" +
        f"&date={settings.DATE}" +
        f"&filter_limit={settings.FILTER_LIMIT}" +
        f"&flat={settings.FLAT}" +
        f"&format={settings.FORMAT}" +
        f"&idSite={settings.ID_SITE}" +
        f"&method={settings.METHOD}" +
        f"&module={settings.MODULE}" +
        f"&period={settings.PERIOD}" +
        f"&token_auth={settings.TOKEN}"
    )
    uri += "&format_metrics=1" if settings.FORMAT_METRICS else ""
    uri += "&expanded=1" if settings.EXPANDED else ""
    return uri


def get_week_total_visits():
    return report['reportTotal']['nb_visits']


def get_avg_visit_time():
    metadata = get_metadata(report)
    return metadata['avg_time_on_site']


def get_bounce_rate():
    metadata = get_metadata(report)
    return metadata['bounce_rate']


def get_metadata(report):
    week_key = list(report['reportData'].keys())[0]
    return report['reportData'][week_key]


main()
