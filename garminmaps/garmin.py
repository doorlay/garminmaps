from typing import List
from garminconnect import Garmin, GarminConnectAuthenticationError
from garth.exc import GarthHTTPError
from getpass import getpass

from activities import Activity
from utils import create_date_range

TOKEN_DIR = "~/.garminmaps"

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


def get_activities(garmin: Garmin, activity_type: str, start_date: str, end_date) -> List[Activity]:
    """Gets all activities of the specified type from the specified date range.

    Args:
        garmin (Garmin): a Garmin object which represents our connection to the Garmin server
        activity_type (str): the type of activity to return data for. Must be one of "running"
        start_date (str): the start date to return activities for. Written in year-month-day, e.g. "2024-03-14"
        end_date (str): the end date to return activities for. Written in year-month-day, e.g. "2024-03-20"
        
    Returns:
        List[Dict]: a list of all activities that match the inputted criteria
    """
    activity_objects = []
    date_range = create_date_range(start_date, end_date)
    for date in date_range:
        response = garmin.get_activities_fordate(date)
        try:
            activities = response["ActivitiesForDay"]["payload"]
        # If no activities of activity_type were recorded on date, skip
        except KeyError:
            pass
        for activity in activities:
            if activity["activityType"]["typeKey"] == activity_type:
                activity_objects.append(Activity(activity, garmin))
    return activity_objects
