from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL



class AddPetForm(FlaskForm):
   """Form for adding pets"""

   name = StringField("Pet Name:", validators=[InputRequired(message="Pet Name can't be blank")])
   species = StringField("Species:", validators=[InputRequired(message="Species can't be blank")])
   photo_url = StringField("Photo URL:", validators=[Optional(), URL()])
   age = StringField("Age:", validators=[Optional()])
   notes = StringField("Notes(Optional):", validators=[Optional()])