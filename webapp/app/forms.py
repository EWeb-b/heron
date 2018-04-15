import re
from flask_wtf import Form
from wtforms import validators
from wtforms.validators import (
    DataRequired, EqualTo, NumberRange, Email, Regexp)
from wtforms.fields.html5 import EmailField
from wtforms.fields import (
    TextField, TextAreaField, PasswordField,
    StringField, SubmitField, DateField, IntegerField, SelectField)


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
    name_on_card = StringField('Name on Card', validators=[DataRequired()])
    billing_address = StringField('Billing Address', validators=[DataRequired()])
    card_number = IntegerField('Card Number', validators=[DataRequired()])
    cvc = IntegerField('CVC', validators=[DataRequired()])
    expiry_date_month = IntegerField('Expiry Date Month', validators=[DataRequired()])
    expiry_date_year = IntegerField('Expiry Date Year', validators=[DataRequired()])
    submit = SubmitField('Add Card')


class ChangePasswordForm(Form):
    prev_password = PasswordField(
        'Previous Password', validators=[DataRequired()])
    new_password = PasswordField(
        'new_password', validators=[DataRequired()])
    confirmation = PasswordField(
        'confirmation',
        validators=[DataRequired(), EqualTo(
            'new_password', message='Passwords need to match')])
    submit = SubmitField('Change Password')


class Search(Form):
    film = StringField('Search Film', validators=[DataRequired()])
    submit = SubmitField('Search')


class OrderTicket(Form):
    ticketType = SelectField('Ticket Type',
                             choices=[('standard', 'Standard'), ('child', 'Child'),
                                      ('student', 'Student'), ('oap', 'OAP')],
                             validators=[DataRequired()])
    # seatNumber = widgets.CheckboxInput()

    submit = SubmitField('Order Ticket')
