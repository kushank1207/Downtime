#codes related to pages before authentication
from flask import Blueprint, render_template, redirect, url_for
from .models import Event, Prize
from datetime import datetime

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    # Select all of events
    events = Event.query.all() #TODO: Filter by date
    prizes = Prize.query.filter(Prize.quantity > 0)

    # Format the date
    for event in events:
        event1 = datetime.strptime(event.start_date, "%Y-%m-%dT%H:%M")
        event.start_date = event1.strftime("%b %d, %Y")
    return render_template("home.html", events=events, prizes=prizes)

