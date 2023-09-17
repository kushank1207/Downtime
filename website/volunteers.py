#codes related to organizers
from flask import Blueprint, render_template, redirect, url_for, request
from datetime import datetime
from . import db
from .models import Event, User, Prize
from sqlalchemy import select
from flask_login import login_required, current_user

volunteers = Blueprint("volunteers", __name__)

@volunteers.route("/")
@volunteers.route("/home") #TODO: Change below
@login_required
def home():
    events = Event.query.all()
    prizes = Prize.query.filter(Prize.quantity > 0)
    previous_attended_events, future_events = [], []
    for event in events:
        event_date = datetime.strptime(event.start_date, '%Y-%m-%dT%H:%M')
        if event_date <= datetime.now():
            previous_attended_events.append(event)
        else:
            future_events.append(event)
        event.start_date = event_date.strftime("%b %d - %H:%M EST")
    return render_template("volunteers.html", user=current_user, previous_attended_events=previous_attended_events, future_events=future_events, available_items=prizes)

# @volunteers.route("/purchase-item")
# def purchase_item():
