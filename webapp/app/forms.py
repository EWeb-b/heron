from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, PasswordField, StringField, SubmitField, FloatField, EmailField
from wtforms.validators import DataRequired, EqualTo, NumberRange

class CreateAccountForm(Form):
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    forename = StringField('Forename', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    card_number = FloatField('Card Number', [validators.DataRequired(), validators.NumberRange(min=0, max=9999999999999999)])
    cvc = FloatField('CVC', [validators.DataRequired(), validators.NumberRange(min=0, max=999)])
    expiry_date_month = DateField('Expiry Date', [validators.DataRequired, validators.NumberRange(min=1, max=12)])
    expiry_date_year = FloatField('Expiry Date Year' [validators.DataRequired, validators.NumberRange(min=2018)])
    submit = SubmitField('Register')

class ChangePasswordForm(Form):
    prev_password = PasswordField('Previous Password', validators=[DataRequired()])
    new_password = PasswordField('new_password', validators=[DataRequired()])
    confirmation = PasswordField('confirmation', validators=[DataRequired(), EqualTo('new_password', message='Passwords need to match')])
    submit = SubmitField('Change Password')

class Search(Form):
    film = StringField('Search Film', validators=[DataRequired()])
    submit = SubmitField('Search')
