# Documentation
### login()
    """Connects to the Garmin server via OAuth2 and returns a Garmin object. This login will generate an OAuth2 login token, valid for one year, and store this on your host in ~/.garminmaps. This token will be used for subsequent logins to avoid needing to re-enter your credentials.
    
    Returns:
        Garmin: a Garmin Connect object.
    """

### create_map()
    """Given an activity, creates a new leaflet.js Map.

    Args:
        [optional] activity (Activity): An Activity Object, representing an activity from Garmin Connect
    Returns:
        Map: The newly created leaflet.js Map, with the activity plotted on it
    """

### get_activities()
    """Gets all activities of the specified type from the specified date range.

    Args:
        garmin (Garmin): a Garmin object which represents our connection to the Garmin server
        activity_type (str): the type of activity to return data for. Must be one of "running"
        start_date (str): the start date to return activities for. Written in year-month-day, e.g. "2024-03-14"
        end_date (str): the end date to return activities for. Written in year-month-day, e.g. "2024-03-20"

    Returns:
        List[Dict]: a list of all activities that match the inputted criteria
    """

### update_map()
    """Given an activity and a Folium map, plots the activity on the map.

    Args:
        activity (Activity): An Activity Object, representing an activity from Garmin Connect
        activity_map (Map): A leaflet.js Map
        line_color (str): The color to plot onto the map. Must be one of {"red", "blue", "green", "yellow"}
    """


# Examples
1. Plot all runs from June 2024 onto a leaflet.js map.

```
import garminmaps

# Login to Garmin Connect with OAuth2
garmin_client = garminmaps.login()

# Create a new empty leaflet.js map
running_map = garminmaps.create_map()

# Get data for all runs in June 2024
activites = garminmaps.get_activities(garmin_client, "running", "2024-06-01", "2024-06-30")
for activity in activites:
    update_map(activity, running_map, "red")

# Write the leaflet.js map to disk
running_map.save("runs.html")
```

2. Plot all hikes from summer of 2023 onto a leaflet.js map.

```
import garminmaps

# Login to Garmin Connect with OAuth2
garmin_client = garminmaps.login()

# Create a new empty leaflet.js map
hiking_map = garminmaps.create_map()

# Get data for all hikes in summer of 2023
activites = garminmaps.get_activities(garmin_client, "hiking", "2023-06-01", "2023-10-01")
for activity in activites:
    update_map(activity, hiking_map, "red")

# Write the leaflet.js map to disk
hiking_map.save("hikes.html")
```