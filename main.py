from utils.utils import login
from utils.graphing import create_map

garmin_client = login()
response = garmin_client.get_activities_fordate("2024-05-01")
activity_id = response["ActivitiesForDay"]["payload"][0]["activityId"]
activity_bytes = garmin_client.download_activity(
    activity_id, garmin_client.ActivityDownloadFormat.GPX
)

mymap = create_map(activity_bytes)
mymap.save("index.html")
