from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
from models import db, connect_db
# from forms import AddSnackForm, EmployeeForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "abc123"
debug = DebugToolbarExtension(app)

connect_db(app)

# toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template("home.html")