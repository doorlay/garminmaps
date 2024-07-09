## Setup
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install -r requirements.txt`

## Usage
Run `python3 main.py` to generate an `index.html` file in the root directory of the project. If you do not have a valid Garmin OAuth token, you will be prompted for your Garmin credentials. These credentials will be used to generate an OAuth token, valid for one year, stored in `~/.garminmaps` on your host.

## Contributing
1. Run `ruff format && ruff check` prior to committing code.


## Future Work
- Add support for range-based plotting
- Add markers to map with data for individual runs
- Superimpose activity data onto the graph
- Use Wails to turn this into an actual application. Use in-browser SSO.