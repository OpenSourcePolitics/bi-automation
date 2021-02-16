import settings # noqa
from urilib import get_report
import re


def metrics():
    settings.init()  # noqa
    global report, total_visits
    start_date = str(input("Enter starting day of report: "))
    end_date = str(input("Enter ending day of report: "))
    report = get_report("general", start_date, end_date)
    metrics = {}
    metrics["start_date"] = start_date
    total_visits = get_week_total_visits()
    metrics["total_visits"] = total_visits
    metrics["avg_visit_time"] = get_avg_visit_time()
    metrics["bounce_rate"] = get_bounce_rate()
    metrics["visited_urls_visits"] = get_visited_urls_number_of_visits(
        settings.get_pages_urls()
    )
    metrics["referrer_report"] = get_referrers_repartition(
        get_report("referrers")
    )

    return metrics


def get_referrers_repartition(referrers, percent=.05):
    main_referrers = []
    for referrer in referrers:
        if is_above_n_percent(referrer['nb_visits'], percent):
            main_referrers.append({
                referrer["label"]: referrer["nb_visits"]
            })
            if referrer.get("subtable"):
                if referrer["label"] == "Social Networks":
                    percent = 0
                else:
                    percent = .05
                main_referrers.append(
                    get_referrers_repartition(referrer["subtable"], percent)
                )

    return main_referrers


def is_above_n_percent(referrer_visits_number, percent=.05):
    return (referrer_visits_number / total_visits) >= percent


def get_visited_urls_number_of_visits(pages_urls=[]):
    visits_per_url = {}
    pages_report = get_report("pages")
    report_data = pages_report['reportData']
    for page_url in pages_urls:
        visits_per_url[page_url] = 0
        for page in report_data:
            if re.match(page_url, page['label']):
                visits_per_url[page_url] += page["nb_visits"]
    return visits_per_url


def get_week_total_visits():
    return report['reportData']['nb_visits']


def get_avg_visit_time():
    return report['reportData']['avg_time_on_site']


def get_bounce_rate():
    return report['reportData']['bounce_rate']
