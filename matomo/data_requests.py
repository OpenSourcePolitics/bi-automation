import settings # noqa
from urilib import get_report


def metrics():
    settings.init()  # noqa
    global report
    start_date = str(input("Enter day of beginning_report"))
    report = get_report("general", start_date=start_date)
    global total_visits
    metrics = {}
    metrics["start_date"] = start_date
    metrics["total_visits"] = get_week_total_visits()
    total_visits = metrics["total_visits"]
    metrics["avg_visit_time"] = get_avg_visit_time()
    metrics["bounce_rate"] = get_bounce_rate()
    pages_urls = ["/processes/transformation-numerique/f/5/","/processes/transformation-numerique/f/2/"]  # noqa
    metrics["visited_urls_visits"] = get_visited_urls_number_of_visit(
        pages_urls
    )
    metrics["referrer_report"] = get_referrers_repartition(
        get_report(
            "referrers",
            start_date=start_date
        )
    )

    return metrics


def get_referrers_repartition(referrers):
    main_referrers = []
    for referrer in referrers:
        if is_above_n_percent(referrer['nb_visits']):
            main_referrers.append({
                referrer["label"]: referrer["nb_visits"]
            })
            if referrer.get("subtable"):
                main_referrers.append(
                    get_referrers_repartition(referrer["subtable"])
                )
    return main_referrers


def is_above_n_percent(referrer_visits_number, percent=.05):
    if (referrer_visits_number / total_visits) >= percent:
        return True
    return False


def get_visited_urls_number_of_visit(pages_urls=[]):
    visits_per_url = {}
    pages_report = get_report("pages")
    report_data = pages_report['reportData']
    for page_url in pages_urls:
        for page in report_data:
            if page['label'] == page_url:
                visits_per_url[page_url] = page["nb_visits"]
    return visits_per_url


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
