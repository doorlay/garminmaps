from typing import Dict, Any
from math import floor

# Helper functions used for all activity classes
def meters_to_miles(distance: float) -> float:
    """Converts meters to miles, returning a float."""
    return distance * 0.000621371


class Run:
    def __init__(self, activity: Dict[str, Any]):
        self.duration = activity["duration"] / 60
        self.distance = meters_to_miles(activity["distance"])
        self.pace = self.calculate_run_pace(self.distance, self.duration)
        self.avg_hr = activity["averageHR"]
        self.start_time = activity["startTimeLocal"]

    def __str__(self):
        data = {
            "start_time": self.start_time,
            "distance": self.distance,
            "duration": self.duration,
            "pace": self.pace,
            "avg_hr": self.avg_hr,
        }
        return str(data)

    def __repr__(self):
        data = {
            "start_time": self.start_time,
            "distance": self.distance,
            "duration": self.duration,
            "pace": self.pace,
            "avg_hr": self.avg_hr
        }
        return str(data)

    def calculate_run_pace(self, distance: float, duration: float) -> str:
        """Given distance in miles and duration in minutes, calculates run pace."""
        pace_minutes = duration / distance
        pace_seconds = str(int((pace_minutes - floor(pace_minutes)) * 60))
        # If less than 10 seconds, prepend a 0 for formatting
        if len(pace_seconds) == 1:
            pace_seconds = f"0{pace_seconds}"
        return f"{floor(pace_minutes)}:{pace_seconds}"
