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
    email = StringField(
        'Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class CreateAccountForm(Form):
    email = EmailField(
        'Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordCheck = PasswordField('Password Confirmation', validators=[DataRequired()])
    submit = SubmitField('Register')

class Profile(Form):
    forename = StringField('Forename', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])

class CardDetails(Form):
    password = PasswordField('Password', validators=[DataRequired()])
    name_on_card = StringField('Name on Card',
        validators=[DataRequired()])
    billing_address = StringField('Billing Address',
        validators=[DataRequired()])
    card_number = IntegerField(
        'Card Number',
        [validators.DataRequired(), validators.Regexp(r'[0-9]{16}$')])
    cvc = IntegerField(
        'CVC',
        [validators.DataRequired(), validators.Regexp(r'[0-9]{3}$')])
    expiry_date_month = DateField(
        'Expiry Date Month',
        [validators.DataRequired, validators.NumberRange(min=1, max=12)])
    expiry_date_year = IntegerField(
        'Expiry Date Year',
        [validators.DataRequired, validators.NumberRange(min=2018)])
    submit = SubmitField('Add Card')


class ChangePasswordForm(Form):
    prev_password = PasswordField(
        'Previous Password', validators=[DataRequired()])
    new_password = PasswordField(
        'new_password', validators=[DataRequired()])
    confirmation = PasswordField(
        'confirmation',
        validators=[DataRequired(),EqualTo(
            'new_password', message='Passwords need to match')])
    submit = SubmitField('Change Password')


class Search(Form):
    film = StringField('Search Film', validators=[DataRequired()])
    submit = SubmitField('Search')

class OrderTickets(Form):
    standard_tickets = IntegerField(
        'Standard Tickets',
        [validators.DataRequired(), validators.NumberRange(max=10)])
    oap_tickets = IntegerField(
        'OAP Tickets',
        [validators.DataRequired(), validators.NumberRange(max=10)])
    child_tickets = IntegerField(
        'Child Tickets',
        [validators.DataRequired(), validators.NumberRange(max=10)])
    cvc_check = IntegerField(
        'CVC Security Check',
        [validators.DataRequired(), validators.Regexp(r'[0-9]{3}$')])
    submit = SubmitField('Order Tickets')
