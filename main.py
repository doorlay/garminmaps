from datetime import datetime, timedelta
from json import loads
from pandas import date_range
from typing import Dict, List
from garminconnect import Garmin

# Import custom-defined activity objects
from activities import Run


def string_to_datetime(date: str) -> datetime:
    """Converts a string in year-month-day format to a datetime object."""
    return datetime.strptime(date, '%Y-%m-%d').date()


def create_date_range(start_date: str, end_date: str) -> List[str]:
    """Given a start and end date, returns a list of all dates in between, inclusive."""
    start_datetime = string_to_datetime(start_date)
    end_datetime = string_to_datetime(end_date)
    return date_range(start_datetime,end_datetime-timedelta(days=1), freq='d').strftime('%Y-%m-%d').tolist()


def get_credentials() -> Dict[str, str]:
    """Reads account credentials from the credentials.env file, returns in a dict."""
    with open("credentials.env") as creds_file:
        creds = loads(creds_file.readline())
        return creds


def meters_to_miles(distance: float) -> float:
    """Converts meters to miles, returning a float."""
    return distance * 0.000621371


def connect_to_garmin() -> Garmin:
    """Connects to the Garmin server and returns a Garmin object."""
    creds = get_credentials()
    garmin = Garmin(creds["email"], creds["password"])
    garmin.login()
    return garmin


def get_activities_by_type_and_date(garmin: Garmin, activity_type: str, date: str) -> List[Dict]:
    """Gets all activities of the specified type on the specified day.

    Args:
        garmin (Garmin): a Garmin object which represents our connection to the Garmin server
        activity_type (str): the type of activity to return data for. Must be one of "running"
        date (str): the date to return activities for. Written in year-month-day, e.g. "2024-03-14"

    Returns:
        List[Dict]: a list of all activities that match the inputted criteria
    """
    response = garmin.get_activities_fordate(date)
    activities = response["ActivitiesForDay"]["payload"]
    ret = []
    for activity in activities:
        if activity["activityType"]["typeKey"] == activity_type:
            ret.append(activity)
    return ret


def get_activities_by_type_and_daterange(garmin: Garmin, activity_type: str, 
                                         start_date: str, end_date: str) -> List[Dict]:
    """Gets all activities of the specified type from the specified date range.

    Args:
        garmin (Garmin):  a Garmin object which represents our connection to the Garmin server
        activity_type (str): the type of activity to return data for. Must be one of "running"
        start_date (str): the first date to return activities for. Written in year-month-day, e.g. "2024-03-14"
        end_date (str): the last date to return activities for. Written in year-month-day, e.g. "2024-03-14"

    Returns:
        List[Dict]: a list of all activities that match the inputted criteria
    """
    ret = []
    date_range = create_date_range(start_date, end_date)
    for date in date_range:
        activites = get_activities_by_type_and_date(garmin, activity_type, date)
        ret += activites
    return ret


garmin = connect_to_garmin()
activities = get_activities_by_type_and_daterange(garmin, "running", "2024-05-01", "2024-06-22")
for activity in activities:
    run = Run(activity)
    print(run)
