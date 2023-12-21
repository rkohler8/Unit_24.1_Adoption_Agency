from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, Length, NumberRange

# ages = ['N/a', 0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

class AddPetForm(FlaskForm):
   """Form for adding pets"""

   name = StringField("Pet Name:", validators=[InputRequired(message="Pet Name can't be blank")])
   # species = StringField("Species:", validators=[InputRequired(message="Species can't be blank")])
   species = SelectField("Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )
   photo_url = StringField("Photo URL:", validators=[Optional(), URL()])
   age = StringField("Age:", validators=[Optional(), NumberRange(min=0, max=30)])
   # age = SelectField("Age:", choices=[(age, age) for age in ages])
   notes = StringField("Notes(Optional):", validators=[Optional(), Length(min=10)])


class EditPetForm(FlaskForm):
   """Form for editing pet details"""

   photo_url = StringField("Photo URL:", validators=[Optional(), URL()])
   # age = StringField("Age:", validators=[Optional()])
   notes = StringField("Notes(Optional):", validators=[Optional()])
   available = BooleanField("Available?")