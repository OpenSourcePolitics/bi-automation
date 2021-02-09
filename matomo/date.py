from datetime import date, timedelta, datetime


def get_report_dates(beginning_day_of_report=date.today()):
    start_date = (
        beginning_day_of_report - timedelta(beginning_day_of_report.weekday())
    )
    end_date = start_date + timedelta(6)
    return (
        f"{start_date.strftime('%Y-%m-%d')},{end_date.strftime('%Y-%m-%d')}"
    )


def serialize_date(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y").date()
