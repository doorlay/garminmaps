import folium
import gpxpy

from utils.utils import connect_to_garmin


garmin_client = connect_to_garmin()
response = garmin_client.get_activities_fordate("2024-05-01")
activity_id = response["ActivitiesForDay"]["payload"][0]["activityId"]
activity_bytes = garmin_client.download_activity(
    activity_id, garmin_client.ActivityDownloadFormat.GPX
)

# Write gpx data to a file
with open("graphs/gpx-file.gpx", "wb") as gpx_file:
    gpx_file.write(activity_bytes)


# Read from the gpx file and replot the data onto a separate leaflet.js graph
gpx_file = open("graphs/gpx-file.gpx", "r")
gpx = gpxpy.parse(gpx_file)
points = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            points.append(tuple([point.latitude, point.longitude]))
latitude = sum(p[0] for p in points) / len(points)
longitude = sum(p[1] for p in points) / len(points)
myMap = folium.Map(
    location=[latitude, longitude], zoom_start=100, tiles="cartodb positron"
)
folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(myMap)

# Save the new graph onto a index.html
myMap.save("graphs/index.html")
