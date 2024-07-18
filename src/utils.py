from datetime import datetime, timedelta
from pandas import date_range
from typing import List


def string_to_datetime(date: str) -> datetime:
    """Converts a string in year-month-day format to a datetime object."""
    return datetime.strptime(date, "%Y-%m-%d").date()


def create_date_range(start_date: str, end_date: str) -> List[str]:
    """Given a start and end date, returns a list of all dates in between, inclusive."""
    start_datetime = string_to_datetime(start_date)
    end_datetime = string_to_datetime(end_date)
    return (
        date_range(start_datetime, end_datetime - timedelta(days=1), freq="d")
        .strftime("%Y-%m-%d")
        .tolist()
    )
