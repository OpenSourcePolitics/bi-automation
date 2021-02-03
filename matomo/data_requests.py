import settings # noqa
from urilib import get_report
from pprint import pprint


def main():
    settings.init()  # noqa
    global report
    report = get_report()
    pprint(get_week_total_visits())
    pprint(get_avg_visit_time())
    pprint(get_bounce_rate())

    pages_urls = ["/processes/transformation-numerique/f/5/","/processes/transformation-numerique/f/2/"]  # noqa
    get_visited_urls_number_of_visit(pages_urls)


def get_visited_urls_number_of_visit(pages_urls=[]):
    pages_report = get_report("pages")
    report_data = pages_report['reportData']
    for page_url in pages_urls:
        for page in report_data:
            if page['label'] == page_url:
                print(f"{page_url} visited {page['nb_visits']} times")  # noqa


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
