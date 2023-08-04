"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()

DEFAULT_IMAGE = 'https://www.personality-insights.com/wp-content/uploads/2017/12/default-profile-pic-150x150.jpg'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.Text,
                           nullable=False)

    last_name = db.Column(db.Text,
                           nullable=False)

    image_url = db.Column(db.Text,
                           nullable=False,
                           default=DEFAULT_IMAGE)
