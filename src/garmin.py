from typing import Dict, List, Any
from garminconnect import Garmin, GarminConnectAuthenticationError
from garth.exc import GarthHTTPError
from getpass import getpass

TOKEN_DIR = "~/.activitymaps-garmin"

from src.utils import create_date_range


def get_mfa():
    """Get MFA."""
    return input("MFA one-time code: ")


def login() -> Garmin:
    """Connects to the Garmin server via OAuth2 and returns a Garmin object."""
    try:
        # Attempt to resume an active session, if there is one
        garmin = Garmin()
        garmin.login(TOKEN_DIR)
    except (FileNotFoundError, GarthHTTPError, GarminConnectAuthenticationError):
        # If session is expired or has never been established, relogin and save session details to ~/.garminmaps
        # If your account has MFA enabled, you'll be prompted during the login
        email = input("Email: ")
        password = getpass("Password: ")
        garmin = Garmin(email=email, password=password, is_cn=False, prompt_mfa=get_mfa)
        garmin.login()
        garmin.garth.dump(TOKEN_DIR)
    return garmin


def convert_to_class(activity: Dict[str, Any]):
    """Converts an activity object returned by the Garmin API to a custom class"""
    activity_type = activity["activityType"]["typeKey"]
    if activity_type == "running":
        return Run(activity)


def get_activities(garmin: Garmin, activity_type: str, date: str) -> List[Dict]:
    """Gets all activities of the specified type on the specified day.

    Args:
        garmin (Garmin): a Garmin object which represents our connection to the Garmin server
        activity_type (str): the type of activity to return data for. Must be one of "running"
        date (str): the date to return activities for. Written in year-month-day, e.g. "2024-03-14"

    Returns:
        List[Dict]: a list of all activities that match the inputted criteria
    """
    response = garmin.get_activities_fordate(date)
    ret = []
    try:
        activities = response["ActivitiesForDay"]["payload"]
    # If no activities of activity_type were recorded on date, return empty list
    except KeyError:
        return ret
    for activity in activities:
        if activity["activityType"]["typeKey"] == activity_type:
            ret.append(activity)
    return ret


def get_activity_ids(garmin: Garmin, activity_type: str, date: str) -> List[str]:
    """Given a date and a type of activity, returns the activity id for all activites that match the criteria."""
    response = garmin.get_activities_fordate(date)
    try:
        activities = response["ActivitiesForDay"]["payload"]
    # If no activities of activity_type were recorded on date, return empty list
    except KeyError:
        return []
    return [
        activity["activityId"]
        for activity in activities
        if activity["activityType"]["typeKey"] == activity_type
    ]


def get_activities_range(
    garmin: Garmin, activity_type: str, start_date: str, end_date: str
) -> List[Dict]:
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
        activities = get_activities(garmin, activity_type, date)
        for activity in activities:
            ret.append(convert_to_class(activity))
    return ret
