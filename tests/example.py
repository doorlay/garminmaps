from garminmaps.garmin import login, get_activity_ids
from garminmaps.utils import create_date_range
from garminmaps.mapping import create_map, plot_on_map


"""Example 1: Plot all runs from June 2024 onto a leaflet.js map."""

# Login to Garmin Connect with OAuth2
garmin_client = login()

# Get activity ids for each run in June
activity_ids = []
date_range = create_date_range("2024-06-01", "2024-06-30")
for date in date_range:
    activity_ids.extend(get_activity_ids(garmin_client, "running", date))

# Get the GPX files, in bytes, for each run
gpx_bytes = [] 
for activity_id in activity_ids:
    gpx_bytes.append(garmin_client.download_activity(activity_id, garmin_client.ActivityDownloadFormat.GPX))
    
# Plot all of the runs on a new leaflet.js map
running_map = create_map()
for gpx in gpx_bytes:
    plot_on_map(gpx, running_map)

# Write the leaflet.js map to disk
running_map.save("graphs/runs.html")



"""Example 2: Plot hikes from the summer of 2023 onto a leaflet.js map."""

# Login to Garmin Connect with OAuth2
garmin_client = login()

# Get activity ids for each run in June
activity_ids = []
date_range = create_date_range("2023-06-01", "2023-09-01")
for date in date_range:
    activity_ids.extend(get_activity_ids(garmin_client, "hiking", date))

# Get the GPX files, in bytes, for each run
gpx_bytes = [] 
for activity_id in activity_ids:
    gpx_bytes.append(garmin_client.download_activity(activity_id, garmin_client.ActivityDownloadFormat.GPX))
    
# Plot all of the runs on a new leaflet.js map
running_map = create_map()
for gpx in gpx_bytes:
    plot_on_map(gpx, running_map)

# Write the leaflet.js map to disk
running_map.save("graphs/hikes.html")
