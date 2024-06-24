## Initial Setup
1. Run the setup script with `./setup.sh`.
2. Put your credentials in a credentials.env file in the following format: `{"email": "<your garmin email>", "password": "<your garmin password>"}`

## Running the Program
1. Begin by activating your virtual environment: `source bin/activate`
2. Run `python3 main.py`.
3. When finished, deactivate your virtual environment: `deactivate`

## Example
1. Begin by running the Flask application locally: `flask --app backend/main run`
2. Make a call to the following endpoint: `http://127.0.0.1:5000/activity?activity_type=running&start_date=2024-05-01&end_date=2024-06-01`

## Future Work
- Week by week view of my activity history, like google calendar.
- Running training goals plotted, with comparison to workouts
- Bar chart visualizations for all activity data