from flask import render_template, flash, redirect, request, Flask, url_for, make_response,session
from app import app, db, models
from .forms import CreateAccountForm, ChangePasswordForm, LogInForm
from .models import UserInfo, FilmDetails, FilmScreenings
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import datetime
import logging

logging.basicConfig(filename='website.log', format= '%(asctime)s%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y|%I:%M:%S', filemode='w', level=logging.DEBUG)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(email):
    return UserInfo.query.filter(email = email).first()


@app.route('/')
@app.route('/index')
def index():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LogInForm()
    if request.method == 'GET':
        return render_template('login.html', title='Log In', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            # sets user to email in database
            user = UserInfo.query.filter_by(email=form.email.data).first()
            if user:  # if user exists
                # checks password with database
                if user.password == form.password.data:
                    login_user(user)  # logs in
                    flash("Logged in successfully")
                    logging.info('%s logged in successfully', user.email)
                    return redirect('/account')

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
        if form.validate_on_submit():
            newuser = User.query.filter_by(email=form.email.data).first()
            if newuser is not None:
                flash("That email has already been used, try a different one")
                return redirect('/create_account')
            else:
                newuser = UserInfo(
                    form.email.data,
                    form.password.data,
                    form.forename.data,
                    form.surname.data,
                    form.date_of_birth.data,
                    form.card_number.data,
                    form.cvc.data,
                    form.expiry_date_month.data,
                    form.expiry_date_year.data)
                db.session.add(newuser)
                db.session.commit()
                login_user(newuser)

                flash("Account created successfully")
                logging.info('New account created. Email: %s', newuser.email)
                return redirect('/account')
        else:  # when there's an error validating
            flash("Error creating your account, please try again")
            # logging.info()
            return redirect('/create_account')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    logging.info('User %s logged out', current_user.email)
    flash("Logged out successfully")
    return redirect('/login')


@app.route('/password_change', methods=['GET', 'POST'])
@login_required
def password_change():
    form = ChangePasswordForm()
    if request.method == 'GET':
        return render_template('password_change.html', title='Change Password', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            user=UserInfo.query.filter_by(email=current_user.email).first()
            if user.password == form.current_password.data:
                if form.new_password.data == form.new_password_check.data:
                    user.password = form.new_password.data
                    logging.info('%s changed their password', user.forename)
                    db.session.commit()
                    flash('Password changed successfully')
                    return redirect('/account')
                else:
                    flash("Passwords don't match")
                    return redirect('/password_change')
            else:
                flash('Incorrect password')
                return redirect('/password_change')
        else:
            flash('Inputs Missing')
            logging.warning(
                'Change password error for %s: form validation error',
                current_user.username)
            return redirect('/change_password')


@app.route('/api/movies', methods=['GET'])
def apiGetMovies():
    """Returns all films in then database in JSON format

    Returns: A JSON object containing details of all films in the database
    """
    movies = FilmDetails.query.all()
    return jsonify(FilmDetails.serializeList(movies))


@app.route('/api/movies/add', methods=['POST'])
def apiNewMovie():
    """Adds a new film to the database via a POST request containing JSON data
    for the new movie"""
    if not request.json or 'film_name' not in request.json:
        abort(404)
    movie = FilmDetails(**request.json)
    db.session.add(movie)
    db.session.commit()
    return 'test', 201
