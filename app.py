from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


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
         age = form.age.data or None
         notes = form.notes.data

         pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
         db.session.add(pet)
         db.session.commit()
         flash(f"New {species} '{name}' Added!")
         return redirect('/')
   else:
         return render_template("add_pet_form.html", form=form)
   
# WTForms gives us lots of useful validators; we want to use these for validating our fields more carefully:

# the species should be either “cat”, “dog”, or “porcupine”
# the photo URL must be a URL (but it should still be able to be optional!)
# the age should be between 0 and 30, if provided
   



# Make a page that shows some information about the pet:

# Name
# Species
# Photo, if present
# Age, if present
# It should also show a form that allows us to edit this pet:

# Photo URL
# Notes
# Available
# This should be at the URL /[pet-id-number]. Make the homepage link to this.
   
@app.route('/<int:id>', methods=["GET", "POST"])
def edit_employee(id):
   pet = Pet.query.get_or_404(id)
   form = EditPetForm(obj=pet)
   #  depts = [(d.dept_code, d.dept_name) for d in Department.query.all()]
   #  form.dept_code.choices = depts

   if form.validate_on_submit():
      pet.notes = form.notes.data
      pet.photo_url = form.photo_url.data
      pet.available = form.available.data
      db.session.commit()
      flash(f"'{pet.name}' updated!")
      return redirect(f'/{pet.id}')
   else:
      return render_template("edit_pet_form.html", form=form, pet=pet)