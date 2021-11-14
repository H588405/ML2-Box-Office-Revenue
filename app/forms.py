from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):
    
    number_of_genres = IntegerField('How many genres does the movie have', validators=[NumberRange(min=0, max=7)])
    runtime = IntegerField('How long is the movie in minutes', validators=[DataRequired()])
    cast_count = IntegerField('How many cast members are there in the movie', validators=[DataRequired()])
    crew_count = IntegerField('How many crew members are there in the movie', validators=[DataRequired()])

    has_collection = SelectField('movie has a collection or not', choices=[(1, 'yes'), (0, 'no')])
    speaks_english = SelectField('Main language in the movie is english', choices=[(1, 'yes'), (0, 'no')])


    budget = FloatField('What is the budget for the movie', validators=[DataRequired()])
    popularity = FloatField('how popular is the movie', validators=[DataRequired()])

    submit = SubmitField('Submit')