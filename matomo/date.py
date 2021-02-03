from datetime import date, timedelta


def get_report_dates(now=date.today()):
    start_date = now - timedelta(now.weekday())
    end_date = start_date + timedelta(6)
    return (
        f"{start_date.strftime('%Y-%m-%d')},{end_date.strftime('%Y-%m-%d')}"
    )
