from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
   """Home Page; Lists all Pets and availability"""
   pets = Pet.query.all()

   return render_template("home.html", pets=pets)

# Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

# Pet name
# Species
# Photo URL
# Age
# Notes
# This should be at the URL path /add. Add a link to this from the homepage

@app.route('/add', methods=["GET", "POST"])
def add_pet():
   form = AddPetForm()
   if form.validate_on_submit():
         name = form.name.data
         species = form.species.data
         photo_url = form.photo_url.data or None
         age = form.age.data
         notes = form.notes.data

         pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
         db.session.add(pet)
         db.session.commit()
         flash(f"New {species} '{name}' Added!")
         return redirect('/')
   else:
         return render_template("add_pet_form.html", form=form)