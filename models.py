from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
   db.app = app
   db.init_app(app)
   app.app_context().push()

DEFAULT_IMAGE = "https://cdn.mos.cms.futurecdn.net/kGnEPHCDjmD97fz2bMtGVc-1200-80.jpg"


# MODELS GO BELOW!
class Pet(db.Model):
   """Pet Model"""

   __tablename__ = "pets"

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.Text, nullable=False)
   species = db.Column(db.Text, nullable=False)
   photo_url = db.Column(db.Text, default=DEFAULT_IMAGE)
   age = db.Column(db.Integer)
   notes = db.Column(db.Text)
   available = db.Column(db.Boolean, nullable=False, default=True)


# id: auto-incrementing integer
# name: text, required
# species: text, required
# photo_url: text, optional
# age: integer, optional
# notes: text, optional
# available: true/false, required, should default to available