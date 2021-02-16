from datetime import datetime, date


def set_report_dates(beginning_day_of_report, ending_day_of_report):
    start_date = beginning_day_of_report
    end_date = ending_day_of_report
    return (
        f"{start_date.strftime('%Y-%m-%d')},{end_date.strftime('%Y-%m-%d')}"
    )


def serialize_date(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y").date()
