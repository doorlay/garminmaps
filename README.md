## Setup
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install -r requirements.txt`

## Usage
Run `python3 main.py` to generate an `index.html` file in the root directory of the project. If you do not have a valid Garmin OAuth token, you will be prompted for your Garmin credentials. These credentials will be used to generate an OAuth token, valid for one year, stored in `~/.garminmaps` on your host.

## Contributing
Run `ruff format && ruff check` prior to committing code.


## Future Work
- Add support for range-based plotting
- Superimpose activity data onto the graph
- Use Wails to turn this into an actual application. Use in-browser SSO.
- Drop down menu in the upper left for each type of activity, color-coded. When you select a type, only those types are displayed
- For each activity type, group activities in a similar location and allow selection of that location. When selected, navigate to that region on the map.
- For each activity, display information on click. e.g. when you click on a run, you get distance, pace, bpm, calories burned, etc. 
