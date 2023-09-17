#codes related to sponsors
from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import Event, User, Prize
from sqlalchemy import select
from flask_login import login_required, current_user

sponsors = Blueprint("sponsors", __name__)

@sponsors.route("/",  methods=["GET", "POST"])
@sponsors.route("/home", methods=["GET", "POST"])
@login_required
def home():
    prizes = Prize.query.all()

    if request.method == 'POST':
        prize_name = request.form.get("prizeTitle")
        hours_need = request.form.get("hoursRequired")
        description = request.form.get("description")
        quantity = request.form.get("quantity")

        user_id = current_user.id

        if prize_name and hours_need and user_id and description and quantity:
            new_prize = Prize(user_id=user_id, prize_name=prize_name, hours_need=hours_need, description=description, quantity=quantity)
            db.session.add(new_prize)
            db.session.commit()
            return redirect(url_for('sponsors.home'))

    return render_template("sponsors.html", name=current_user.name, prizes=prizes)