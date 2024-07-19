<!-- ## Usage
Run `pip install garminmaps` to install.

Example usage:
```
import garminmaps

"""Example: Plot all runs from June 2024 onto a leaflet.js map."""

# Login to Garmin Connect with OAuth2
garmin_client = garminmaps.login()

# Create a new empty leaflet.js map
running_map = garminmaps.create_map()

# Get data for all runs in June 2024
activites = garminmaps.get_activities(garmin_client, "running", "2024-06-01", "2024-06-30")
for activity in activites:
    activity.plot(running_map)

# Write the leaflet.js map to disk
running_map.save("runs.html")
``` -->

## Dev setup
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install -r requirements.txt`

## Dev release
1. Prior to commiting code, run `ruff format && ruff check`
2. `python3 -m build`
3. Upload the tarball in the dist folder to [PyPi](https://pypi.org/).

## Future Work
- Add support for range-based plotting
- Superimpose activity data onto the graph
- Use Wails to turn this into an actual application. Use in-browser SSO.
- Drop down menu in the upper left for each type of activity, color-coded. When you select a type, only those types are displayed
- For each activity type, group activities in a similar location and allow selection of that location. When selected, navigate to that region on the map.
- For each activity, display information on click. e.g. when you click on a run, you get distance, pace, bpm, calories burned, etc. 
- hand-roll GPX parsing to lower dependencies. Maybe the same for mapping, auth