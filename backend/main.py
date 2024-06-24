import json
from flask import Flask, request
from utils import connect_to_garmin, get_activities_range

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/activity")
def get_activity():
    garmin_client = connect_to_garmin()
    activity_type = request.args.get("activity_type", "")
    start_date = request.args.get("start_date", "")
    end_date = request.args.get("end_date", "")
    activities = get_activities_range(garmin_client, activity_type, start_date, end_date)
    return json.dumps(
            activities,
            default=lambda o: o.__dict__, 
            sort_keys=True,
    )
