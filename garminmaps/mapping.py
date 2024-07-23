from folium import Map, PolyLine, Marker, Icon, Popup
from gpxpy import parse

from garminmaps.activities import Activity
from garminmaps.utils import create_activity_summary


def create_map(activity: Activity = None) -> Map:
    """Given an activity, creates a new leaflet.js Map.

    Args:
        [optional] activity (Activity): An Activity Object, representing an activity from Garmin Connect
    Returns:
        Map: The newly created leaflet.js Map, with the activity plotted on it
    """
    # If activity_bytes not supplied, create an empty Map
    if activity is None:
        return Map(zoom_start=100, tiles="cartodb positron")
    # If activity_bytes is supplied, create a Map and plot the activity
    gpx = parse(activity.gpx)
    points = []
    start_coord = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # Track the coordinates of the start of the activity
                if not start_coord:
                    start_coord.append(point.latitude)
                    start_coord.append(point.longitude)
                points.append(tuple([point.latitude, point.longitude]))
    avg_latitude = sum(p[0] for p in points) / len(points)
    avg_longitude = sum(p[1] for p in points) / len(points)
    activity_map = Map(
        location=[avg_latitude, avg_longitude],
        zoom_start=100,
        tiles="cartodb positron",
    )
    PolyLine(points, color="red", weight=2.5, opacity=1).add_to(activity_map)
    summary = create_activity_summary(activity)
    Marker(
        location=start_coord,
        tooltip="Click me!",
        popup=summary,
        icon=Icon(icon="cloud"),
    ).add_to(activity_map)
    return activity_map


def update_map(activity: Activity, activity_map: Map, line_color: str) -> None:
    """Given an activity and a Folium map, plots the activity on the map.

    Args:
        activity (Activity): An Activity Object, representing an activity from Garmin Connect
        activity_map (Map): A leaflet.js Map
        line_color (str): The color to plot onto the map. Must be one of {"red", "blue", "green", "yellow"}
    """
    gpx = parse(activity.gpx)
    points = []
    start_coord = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # Track the coordinates of the start of the activity
                if not start_coord:
                    start_coord.append(point.latitude)
                    start_coord.append(point.longitude)
                points.append(tuple([point.latitude, point.longitude]))
    # If Map.location is None, set it now.
    if activity_map.location is None:
        avg_latitude = sum(p[0] for p in points) / len(points)
        avg_longitude = sum(p[1] for p in points) / len(points)
        activity_map.location = [avg_latitude, avg_longitude]
    # Build an activity summary with some additional information
    summary = create_activity_summary(activity)
    PolyLine(points, color=line_color, weight=2.5, opacity=1).add_to(activity_map)
    Marker(
        location=start_coord,
        tooltip="Click me!",
        popup=summary,
        icon=Icon(prefix="fa", icon="person-running"),
    ).add_to(activity_map)
