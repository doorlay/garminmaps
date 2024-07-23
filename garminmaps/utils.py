from datetime import datetime, timedelta
from pandas import date_range
from typing import List
from math import floor

from garminmaps.activities import Activity


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


def meters_to_miles(meters: float):
    return round(meters * 0.000621371, 2)


def create_activity_summary(activity: Activity, metric: bool = False) -> str:
    minutes = activity.duration / 60
    duration_minutes = int(floor(minutes))
    duration_seconds = str(int((minutes - duration_minutes) * 60))
    # Ensure the seconds are formatted properly
    if len(duration_seconds) == 1:
        duration_seconds = f"0{duration_seconds}"
    if metric:
        distance = round(activity.distance / 1000, 2)
    else:
        distance = meters_to_miles(activity.distance)
    return f"Distance: {distance}\nDuration: {duration_minutes}:{duration_seconds}"
