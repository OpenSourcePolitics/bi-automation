import settings
from http_handler import http_get
from date import get_report_dates

from datetime import date, timedelta


def get_report(type="general"):
    settings.DATE = get_report_dates(date.today()-timedelta(7))
    http_request = set_uri(type)
    return http_get(http_request)


def set_uri(request_type):
    if request_type == "general":
        pass
    elif request_type == "pages":
        settings.API_ACTION = "getPageUrls"
        settings.API_MODULE = "Actions"
        settings.FLAT = 1
        settings.PERIOD = "range"
    elif request_type == "referrers":
        settings.API_ACTION = ""
        settings.API_MODULE = ""
        settings.METHOD = "Referrers.getReferrerType"
        settings.EXPANDED = 1
        settings.PERIOD = "range"
    uri = (
        settings.BASE_URL +
        f"apiAction={settings.API_ACTION}" +
        f"&apiModule={settings.API_MODULE}" +
        f"&date={settings.DATE}" +
        f"&filter_limit={settings.FILTER_LIMIT}" +
        f"&format={settings.FORMAT}" +
        f"&idSite={settings.ID_SITE}" +
        f"&method={settings.METHOD}" +
        f"&module={settings.MODULE}" +
        f"&period={settings.PERIOD}" +
        f"&token_auth={settings.TOKEN}"
    )
    uri += "&format_metrics=1" if settings.FORMAT_METRICS else ""
    uri += "&expanded=1" if settings.EXPANDED else ""
    uri += "&flat=1" if settings.FLAT else ""
    return uri
