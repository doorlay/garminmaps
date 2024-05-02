import datetime
import json
import logging
import os
import sys
from getpass import getpass

import readchar
import requests

# from garth.exc import GarthHTTPError
from garminconnect import (
    Garmin,
#     GarminConnectAuthenticationError,
#     GarminConnectConnectionError,
#     GarminConnectTooManyRequestsError,
)

def get_credentials():
    with open("credentials.env") as creds_file:
        creds = json.loads(creds_file.readline())
        return creds

def meters_to_miles(distance):
    return distance * 0.000621371

creds = get_credentials()
garmin = Garmin(creds["email"], creds["password"])
garmin.login()
# Get stats for today

response = garmin.get_activities_fordate("2024-03-14")
activities = response["ActivitiesForDay"]["payload"]
for activity in activities:
    print(activity["activityType"]["typeKey"])
    mileage = meters_to_miles(activity["distance"])
    print(f"Distance: {mileage}")

