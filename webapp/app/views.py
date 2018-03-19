from flask import (
    render_template, flash, redirect, request, Flask, url_for,
    make_response, session)
from flask_bootstrap import Bootstrap
from app import app, db, models
from .forms import CreateAccountForm, ChangePasswordForm, LogInForm, CardDetails
from .models import Account, Profile, Certificate, FilmDetails, FilmScreening, TicketType, Card
from flask_login import (
    LoginManager, login_user, logout_user, login_required, current_user)
import datetime
import hashlib
import logging
from werkzeug.security import generate_password_hash, check_password_hash


logging.basicConfig(
    filename='website.log', format='%(asctime)s%(levelname)s:%(message)s',
    datefmt='%d/%m/%Y|%I:%M:%S', filemode='w', level=logging.DEBUG)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Uses Knuth's Multiplicative Method to hash numbers


def hashNumber(numberToBeHashed):
    string = str(numberToBeHashed)
    hashedNumber = print(hashlib.md5(string.encode('utf-8')).hexdigest())
    return hashedNumber


@login_manager.user_loader
def load_user(user_id):
    return Account.query.filter(Account.id == int(user_id)).first()


@app.route('/')
@app.route('/index')
def index():
    return redirect('/home')


@app.route('/home')
def home():
    return render_template(
        'home.html', title='Heron Home')


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LogInForm()
    if request.method == 'GET':
        return render_template('login.html', title='Log In', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            # sets user to email in database
            user = Account.query.filter_by(email=form.email.data).first()
            if user:  # if user exists
                # checks password with database
                if (check_password_hash(user.password, form.password.data)):
                    print(user.password)
                    login_user(user)  # logs in
                    flash("Logged in successfully")
                    logging.info('%s logged in successfully', user.email)
                    return redirect('/profile')
                else:
                    flash("Incorrect Password")
                    logging.warning('User entered the wrong password')
                    return redirect('/login')
            else:
                flash("User does not exist")
                logging.warning('Unsuccessful login: user does not exist')
                return redirect('/login')
        else:
            flash("Form not validated")
            logging.warning('Unsuccessful login: Form not validated')
            return redirect('/login')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():

    form = CreateAccountForm()
    if request.method == 'GET':
        return render_template(
            'create_account.html', title='Create Account', form=form)

    elif request.method == 'POST':
        print("POST METHOD")
        if form.validate_on_submit():
            print("FORM VALID")
            # storedUser and newuser are not the same - keep them separate
            storedUser = Account.query.filter_by(email=form.email.data).first()
            print(storedUser)
            if storedUser is not None:
                print("foo")
                flash("That email has already been used, try a different one")
                return redirect('/create_account')
            else:
                print("bar")
                if form.password.data == form.passwordCheck.data:
                    print("password matched")
                    newuser = Account(
                        email=form.email.data,
                        password=generate_password_hash(form.password.data),
                        staff=False)
                    print(newuser.password)
                    db.session.add(newuser)
                    db.session.commit()
                    login_user(newuser)
                    print(current_user.id)
                    flash("Account created successfully")
                    logging.info('New account created. Email: %s',
                                 newuser.email)
                    return redirect('/profile')
                else:
                    print("passed didnt match")
                    flash("Passwords don't match")
                    return redirect('/create_account')

        else:  # when there's an error validating
            flash("Error creating your account, please try again")
            # logging.info()
            return redirect('/create_account')


@app.route('/logout')
@login_required
def logout():
    # need the name variable otherwise logging does not work
    name_email = current_user.email
    logout_user()
    logging.info('User %s logged out', name_email)
    flash("Logged out successfully")
    logging.info('%s logged out successfully', name_email)
    return redirect('/login')


@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if request.method == 'GET':
        return render_template(
            'change_password.html', title='Change Password', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():  # if form data entered correctly
            # current_user is a variable name from flask_login:
            # don't need to create a new user object
            if current_user.password == form.prev_password.data:
                current_user.password = form.new_password.data
                db.session.commit()
                flash('Password changed successfully')
                logging.info(
                    '%s successfully changed their password',
                    current_user.email)
                return redirect('/logout')
            else:
                flash('Previous Password is incorrect')
                logging.warning(
                    'Change password error for %s: previous password ' +
                    'is incorrect',
                    current_user.email)
                return redirect('/change_password')
        else:
            flash('Inputs Missing')
            logging.warning(
                'Change password error for %s: form validation error',
                current_user.email)
            return redirect('/change_password')


@app.route('/add_card', methods=['GET', 'POST'])
@login_required
def add_card():
    form = CardDetails()
    if request.method == 'GET':
        return render_template(
            'add_card.html', title='Add Card', form=form)
    elif request.method == 'POST':
        print('POST method')
        if form.validate_on_submit():
            print('form validate_on_submit')
            if (check_password_hash(current_user.password, form.password.data)):
                print('passwords match')
                newCard = Card(
                    name_on_card=form.name_on_card.data,
                    billing_address=form.billing_address.data,
                    card_number=hashNumber(form.card_number.data),
                    cvc=hashNumber(form.cvc.data),
                    expiry_date_month=hashNumber(form.expiry_date_month.data),
                    expiry_date_year=hashNumber(form.expiry_date_year.data)
                )
                print('card created not added')
                db.session.add(newCard)
                db.session.commit()
                print('successfully added card(?)')
                return redirect('/profile')
            else:
                flash('passwords dont match')
                print('passwords didnt match')
                return redirect('/add_card')
        else:
            flash('form did not validate on submit')
            print('form didnt validate on submit')
            return redirect('/add_card')


@app.route('/order_ticket', methods=['GET', 'POST'])
def orderTicket():

    film = models.FilmDetails.query.filter_by(film.filmName).first

    return render_template(
        'order_ticket.html', title='Tickets', film=film)


@app.route('/film_info', methods=['GET', 'POST'])
def film_details():
    passed = request.args.get('passed', None)
    film = models.FilmDetails.query.filter_by(filmName=passed).first_or_404()

    return render_template(
        'filmInfo.html', title='Film Details', film=film)


@app.route('/film_details', methods=['GET', 'POST'])
def list_films():
    # print list of films stored in FilmDetails databse
    filmDetails = models.FilmDetails.query.all()
    # userList = models.Account.query.all()
    return render_template(
        'filmDetails.html', title='Film List', filmDetails=filmDetails)


@app.route('/profile', methods=['GET'])
def profile():

    return render_template(
        'profile.html', title='User Profile')

@app.route('/basket', methods=['GET'])
def basket():

    return render_template(
        'basket.html', title='Checkout')
