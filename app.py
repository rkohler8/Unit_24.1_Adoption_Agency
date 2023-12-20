from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
from models import db, connect_db, Pet
# from forms import AddSnackForm, EmployeeForm


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