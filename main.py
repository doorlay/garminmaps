from datetime import datetime, timedelta
from json import loads
from pandas import date_range
from typing import Dict, List
from garminconnect import Garmin


def string_to_datetime(date: str):
    """Converts a string in year-month-day format to a datetime object."""
    return datetime.strptime(date, '%Y-%m-%d').date()


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


def get_activity_by_type_and_date(garmin: Garmin, activity_type: str, date: str) -> List[Dict]:
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


def get_running_mileage(garmin: Garmin, start_date: str, end_date: str) -> float:
    """Gets the total running mileage over a given range of dates.

    Args:
        garmin (Garmin): a Garmin object which represents our connection to the Garmin server
        start_date (str): the beginning of our range of dates (inclusive). Written in year-month-day, e.g. "2024-03-14"
        end_date (str): the end of our range of dates (inclusive). Written in year-month-day, e.g. "2024-03-14"
    
    Returns:
        float: total running mileage, in miles, over the given range of dates
        
    """
    start_datetime = string_to_datetime(start_date)
    end_datetime = string_to_datetime(end_date)
    d_range = date_range(start_datetime,end_datetime-timedelta(days=1), freq='d').strftime('%Y-%m-%d').tolist()
    total_mileage = 0
    for date in d_range:
        activites = get_activity_by_type_and_date(garmin, "running", date)
        for activity in activites:
            total_mileage += activity["distance"]
    return meters_to_miles(total_mileage)


garmin = connect_to_garmin()
result = get_running_mileage(garmin, "2024-03-14", "2024-03-21")
print(result)


"""
I'd like bar charts that do neat data visualization for me. Probably on a website or an app or something.

So this will likely just be an API for me.

Maybe I'll do PDF visualization or something and upload to a website? That way it'll be static by much easier to do. Not sure yet.

"""