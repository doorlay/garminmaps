from utils.utils import login
from utils.graphing import create_map, plot_on_map

garmin_client = login()

# Get activity 1
response = garmin_client.get_activities_fordate("2024-05-01")
activity_id = response["ActivitiesForDay"]["payload"][0]["activityId"]
activity_bytes_one = garmin_client.download_activity(
    activity_id, garmin_client.ActivityDownloadFormat.GPX
)

# Get activity 2
response = garmin_client.get_activities_fordate("2024-06-23")
activity_id = response["ActivitiesForDay"]["payload"][0]["activityId"]
activity_bytes_two = garmin_client.download_activity(
    activity_id, garmin_client.ActivityDownloadFormat.GPX
)

mymap = create_map(activity_bytes_one)
plot_on_map(activity_bytes_two, mymap)
mymap.save("index.html")
