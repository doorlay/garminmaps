from folium import Map, PolyLine
from gpxpy import parse


def create_map(activity_bytes: bytes) -> Map:
    """Given an activity in bytes, creates a new leaflet.js Map.

    Args:
        activity_bytes (bytes): An GPX file downloaded from Garmin Connect, representing an activity
    Returns:
        Map: The newly created leaflet.js Map, with the activity plotted on it
    """
    gpx = parse(activity_bytes)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    latitude = sum(p[0] for p in points) / len(points)
    longitude = sum(p[1] for p in points) / len(points)
    activity_map = Map(
        location=[latitude, longitude], zoom_start=100, tiles="cartodb positron"
    )
    PolyLine(points, color="red", weight=2.5, opacity=1).add_to(activity_map)
    return activity_map


def plot_on_map(activity_bytes: bytes, activity_map: Map) -> bool:
    """TODO: Implement this function."""
    pass
