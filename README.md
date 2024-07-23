## Overview
garminmaps is an SDK for generating interactive leaflet.js maps from Garmin data.

## Installation
``` 
pip3 install garminmaps
```

## Example usage
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
    update_map(activity, running_map, "blue")

# Write the leaflet.js map to disk
running_map.save("runs.html")
```

## Contributing
Creating a dev environment:
1. Clone this repository.
2. `python3 -m venv .venv`
3. `source .venv/bin/activate`
4. `pip3 install .`

Commiting code:
1. `ruff format && ruff check`
2. Fork the repository, checkout a new branch on your forked version, and push changes.
3. Open a pull request in the [GitHub repository](https://github.com/doorlay/garminmaps/pulls).

Building & releasing to PyPI (author only):
1. Bump the version of the project in `pyproject.toml`.
2. `python3 -m build`
3. To release to TestPyPI: `python3 -m twine upload --repository testpypi dist/*`
4. To release to PyPI: `python3 -m twine upload dist/*`

<!-- ## Future Work
- Add support for range-based plotting
- Superimpose activity data onto the graph
- Use Wails to turn this into an actual application. Use in-browser SSO.
- Drop down menu in the upper left for each type of activity, color-coded. When you select a type, only those types are displayed
- For each activity type, group activities in a similar location and allow selection of that location. When selected, navigate to that region on the map.
- For each activity, display information on click. e.g. when you click on a run, you get distance, pace, bpm, calories burned, etc. 
- hand-roll GPX parsing to lower dependencies. Maybe the same for mapping, auth -->