from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# .env
from dotenv import load_dotenv
load_dotenv()

# database
db = SQLAlchemy()
DB_NAME = "downtime.db"
# End db

# file uploads
# UPLOAD_FOLDER = '../static/uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)

    from .views import views # before auth
    from .auth import auth
    from .volunteers import volunteers
    from .organizers import organizers
    from .sponsors import sponsors

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(volunteers, url_prefix="/volunteers")
    app.register_blueprint(organizers, url_prefix="/organizers")
    app.register_blueprint(sponsors, url_prefix="/sponsors")

    # import tables
    from .models import User, Event, Prize, Volunteer
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app