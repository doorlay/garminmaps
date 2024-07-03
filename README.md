## Setup
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install -r requirements.txt`
4. Put your credentials in a credentials.env file in the following format: `{"email": "<your garmin email>", "password": "<your garmin password>"}`.

## Testing
1. Run the Flask application locally: `flask --app backend/main run`
2. Visit the following link: http://127.0.0.1:5000/activity?activity_type=running&start_date=2024-05-01&end_date=2024-06-01

## Future Work
- Week by week view of my activity history, like google calendar.
- Running training goals plotted, with comparison to workouts
- Bar chart visualizations for all activity data