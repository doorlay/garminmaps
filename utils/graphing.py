from folium import Map, PolyLine, Marker, Icon
from gpxpy import parse


def create_map(activity_bytes: bytes) -> Map:
    """Given an activity in bytes, creates a new leaflet.js Map.

    Args:
        activity_bytes (bytes): A GPX file downloaded from Garmin Connect, representing an activity
    Returns:
        Map: The newly created leaflet.js Map, with the activity plotted on it
    """
    gpx = parse(activity_bytes)
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
        location=[avg_latitude, avg_longitude], zoom_start=100, tiles="cartodb positron"
    )
    PolyLine(points, color="red", weight=2.5, opacity=1).add_to(activity_map)
    Marker(location=start_coord, tooltip="Click me!", popup="Run", icon=Icon(icon="cloud")).add_to(activity_map)
    return activity_map


def plot_on_map(activity_bytes: bytes, activity_map: Map) -> None:
    """Given an activity in bytes and a Folium map, plots the activity on the map.
    
    Args:
        activity_bytes (bytes): An GPX file downloaded from Garmin Connect, representing an activity
        activity_map (Map): A leaflet.js Map
    """
    gpx = parse(activity_bytes)
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
    PolyLine(points, color="red", weight=2.5, opacity=1).add_to(activity_map)
    Marker(location=start_coord, tooltip="Click me!", popup="Run", icon=Icon(icon="cloud")).add_to(activity_map)
