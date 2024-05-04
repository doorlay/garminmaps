from datetime import datetime, timedelta
from json import loads
from math import floor
from pandas import date_range
from typing import Dict, List, Any
from garminconnect import Garmin


def string_to_datetime(date: str) -> datetime:
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


def calculate_run_pace(distance: float, duration: float) -> str:
    """Given distance in miles and duration in minutes, calculates run pace."""
    pace_minutes = duration / distance
    pace_seconds = str(int((pace_minutes - floor(pace_minutes)) * 60))
    # If less than 10 seconds, prepend a 0 for formatting
    if len(pace_seconds) == 1:
        pace_seconds = f"0{pace_seconds}"
    return f"{floor(pace_minutes)}:{pace_seconds}"


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


def get_run_stats(activity: Dict[str, Any]) -> Dict[str, str]:
    """Given a running activity, extracts all interesting stats into a dictionary.

    Args:
        activity(Dict[str, Any]): an activity object as returned from the Garmin server

    Returns:
        Dict[str, str]: a dictionary containing a run's distance in miles, total time, pace, and average heart rate
    """
    distance = meters_to_miles(activity["distance"])
    duration = activity["duration"] / 60
    pace = calculate_run_pace(distance, duration)
    avg_hr = activity["averageHR"]
    return {
        "distance": str(distance),
        "duration": str(duration),
        "pace": pace,
        "avg_hr": str(avg_hr)
    }


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
        activites = get_activities_by_type_and_date(garmin, "running", date)
        for activity in activites:
            total_mileage += activity["distance"]
    return meters_to_miles(total_mileage)


garmin = connect_to_garmin()
activities = get_activities_by_type_and_date(garmin, "running", "2024-03-14")
for activity in activities:
    result = get_run_stats(activity)
    print(result)


"""
I'd like bar charts that do neat data visualization for me. Probably on a website or an app or something.

So this will likely just be an API for me.

Maybe I'll do PDF visualization or something and upload to a website? That way it'll be static by much easier to do. Not sure yet.

"""