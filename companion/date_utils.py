from datetime import date, datetime, timedelta

AUDIT_DEFAULT_DAYS = 45
AUDIT_FIRST_TIME_DAYS = 90
FRESHNESS_CHECK_DAYS = 180


def calculate_cutoff(window_days=AUDIT_DEFAULT_DAYS):
    today = date.today()
    cutoff = today - timedelta(days=window_days)
    return cutoff.isoformat()


def jira_date_filter(cutoff_date):
    return f'AND updated >= "{cutoff_date}"'


def hivemind_date_filter_ms(cutoff_date):
    dt = datetime.fromisoformat(cutoff_date)
    return int(dt.timestamp() * 1000)
