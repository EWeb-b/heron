from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, PasswordField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, EqualTo

class CreateAccountForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class ChangePasswordForm(Form):
    prev_password = PasswordField('Previous Password', validators=[DataRequired()])
    new_password = PasswordField('new_password', validators=[DataRequired()])
    confirmation = PasswordField('confirmation', validators=[DataRequired(), EqualTo('new_password', message='Passwords need to match')])
