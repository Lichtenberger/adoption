from flask_wtf import FlaskFormfrom wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    '''for to add pet'''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    '''edit pets'''

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional(), Length(min=10)])

    available = BooleanField('Available')