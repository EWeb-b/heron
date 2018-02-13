import re
from flask_wtf import Form
from wtforms import validators
from wtforms.validators import (
    DataRequired, EqualTo, NumberRange, Email, Regexp)
from wtforms.fields.html5 import EmailField
from wtforms.fields import (
    TextField, TextAreaField, PasswordField,
    StringField, SubmitField, DateField, IntegerField)

class LogInForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class CreateAccountForm(Form):
    email = EmailField(
        'Email Address', [validators.DataRequired(), validators.Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    forename = StringField('Forename', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', format='%d/%m/%Y', validators=[DataRequired()])
    card_number = IntegerField(
        'Card Number',
        [validators.DataRequired(), validators.Regexp(r'[0-9]{16}$')])

    cvc = IntegerField(
        'CVC',
        [validators.DataRequired(), validators.Regexp(r'[0-9]{3}$')])

    expiry_date_month = DateField(
        'Expiry Date',
        [validators.DataRequired, validators.NumberRange(min=1, max=12)])

    expiry_date_year = IntegerField(
        'Expiry Date Year',
        [validators.DataRequired, validators.NumberRange(min=2018)])

    submit = SubmitField('Register')


class ChangePasswordForm(Form):
    prev_password = PasswordField(
        'Previous Password', validators=[DataRequired()])
    new_password = PasswordField('new_password', validators=[DataRequired()])
    confirmation = PasswordField(
        'confirmation',
        validators=[
            DataRequired(),
            EqualTo('new_password', message='Passwords need to match')])
    submit = SubmitField('Change Password')


class Search(Form):
    film = StringField('Search Film', validators=[DataRequired()])
    submit = SubmitField('Search')
