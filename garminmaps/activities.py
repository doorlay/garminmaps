class Activity:
    def __init__(self, payload, garmin_client):
        self.id = payload["activityId"]
        self.type = payload["activityType"]["typeKey"]
        self.date = self.convert_date(payload["startTimeLocal"])
        self.distance = payload["distance"]
        self.duration = payload["duration"]
        self.gpx = garmin_client.download_activity(
            self.id, garmin_client.ActivityDownloadFormat.GPX
        )

    def convert_date(self, date_raw: str):
        return date_raw.split("T")[0]
