import re
from flask_wtf import Form
from wtforms import validators
from wtforms.validators import (
    DataRequired, EqualTo, NumberRange, Email, Regexp)
from wtforms.fields.html5 import EmailField
from wtforms.fields import (
    TextField, TextAreaField, PasswordField,
    StringField, SubmitField, DateField, IntegerField,
    BooleanField, SelectField)

from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import db, models
from .models import Card


class LogInForm(Form):
    email = EmailField(
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
    password = PasswordField('Password', [validators.DataRequired()])
    name_on_card = StringField('Name on Card', validators=[DataRequired()])
    billing_address = StringField('Billing Address',
                                  validators=[DataRequired()])
    card_number = IntegerField('Card Number', [validators.DataRequired()])
    cvc = IntegerField('CVC', [validators.DataRequired()])
    expiry_date_month = IntegerField('Expiry Date Month',
                                     [validators.DataRequired(),
                                      validators.NumberRange(min=1, max=12)])
    expiry_date_year = IntegerField(
        'Expiry Date Year', [validators.DataRequired(),
                             validators.NumberRange(min=2018)])
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


class Basket(Form):
    first_name = StringField(
        'First Name', validators=[DataRequired()])
    last_name = StringField(
        'Last Name', validators=[DataRequired()])
    address = StringField(
        'Address', validators=[DataRequired()])
    postcode = StringField(
        'Postcode', validators=[DataRequired()])
    card = SelectField('Cards', choices=[], validators=[DataRequired()])
    submit = SubmitField('Order Ticket')


class Search(Form):
    film = StringField('Search Film', validators=[DataRequired()])
    submit = SubmitField('Search')


class ShowTimes(Form):
    times = SelectField('Showing Times',
                        choices=[('10am', '10:00'), ('2pm', '14:00'),
                                 ('8pm', '20:00')],
                        validators=[DataRequired()])
    submit = SubmitField('Order Ticket')


class OrderTicket(Form):
    ticket_type = SelectField('Ticket Type',
                              choices=[('standard', 'Standard'), ('child', 'Child'),
                                       ('student', 'Student'), ('oap', 'OAP')],
                              validators=[DataRequired()])
    seat_number = SelectField('Seat Number',
                              choices=[('1', '1'), ('2', '2'), ('3', '3'),
                                       ('4', '4'), ('5', '5'), ('6', '6'),
                                       ('7', '7'), ('8', '8'),
                                       ('9', '9 (VIP)'),
                                       ('10', '10 (VIP)'),
                                       ('11', '11 (VIP)'),
                                       ('12', '12 (VIP)'),
                                       ('13', '13 (VIP)'),
                                       ('14', '14 (VIP)'),
                                       ('15', '15 (VIP)'),
                                       ('16', '16 (VIP)'),
                                       ('17', '17'), ('18', '18'), ('19', '19'),
                                       ('20', '20'), ('21', '21'), ('22', '22'),
                                       ('23', '23'), ('24', '24')],
                              validators=[DataRequired()])
    submit = SubmitField('Order Ticket')
