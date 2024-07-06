## Setup
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install -r requirements.txt`
4. Put your credentials in a credentials.env file in the following format: `{"email": "<your garmin email>", "password": "<your garmin password>"}`.

## Testing
1. Run `ruff format && ruff check` to format & lint your changes.
2. Run `python3 main.py`.

## Future Work
- Implement Oauth2
- Add support for range-based plotting
- Add markers to map with data for individual runs
- Superimpose activity data onto the graph