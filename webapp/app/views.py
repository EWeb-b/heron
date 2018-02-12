from flask import (
    render_template, flash, redirect, request, Flask, url_for, make_response,
    session, jsonify)
from app import app, db, models
from .forms import CreateAccountForm, ChangePasswordForm
from .models import UserInfo, FilmDetails, FilmScreenings
from flask_login import (
    LoginManager, login_user, logout_user, login_required, current_user)
import datetime
import logging

FORMAT = '%(asctime)s %(levelname)s:%(message)s'
DATEFMT = '%d/%m/%Y %H:%M:%S'
logging.basicConfig(
    filename='example.log', format=FORMAT, datefmt=DATEFMT,
    filemode='w', level=logging.DEBUG)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):

    return User.query.filter(User.holder_id == int(user_id)).first()


@app.route('/')
@app.route('/index')
def index():

    # Redirects the base-level domain to login page
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = CreateAccountForm()
    if request.method == 'GET':
        return render_template('login.html', title='Log In', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            # sets user to username in database
            user = User.query.filter_by(username=form.username.data).first()
            if user:  # if user exists
                # checks password with database one
                if user.password == form.password.data:
                    login_user(user)  # logs in
                    flash("Logged in successfully")
                    logging.info('%s logged in successfully', user.username)
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
            storedUser = User.query.filter_by(
                username=form.username.data).first()
            if storedUser is not None:
                flash("That username already exists, try a different one")
                return redirect('/create_account')
            else:
                newuser = User(
                    form.username.data, form.password.data, accountValue=0.0)
                db.session.add(newuser)
                db.session.commit()
                login_user(newuser)

                flash("Account created successfully")
                logging.info(
                    'New account created. Username: %s', newuser.username)
                return redirect('/account')
        else:  # when there's an error validating
            flash("Problem creating your account, please try again")
            # logging.info()
            return redirect('/create_account')


@app.route('/logout')
@login_required
def logout():
    name = current_user.username
    logout_user()
    flash("Logged out successfully")
    logging.info('%s logged out successfully', name)
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
            # if Previous Password is correct
            if current_user.password == form.prev_password.data:

                current_user.password = form.new_password.data
                db.session.commit()
                flash('Password changed successfully')
                logging.info(
                    '%s successfully changed their password',
                    current_user.username)
                return redirect('/logout')

            else:
                flash('Previous Password is incorrect')
                logging.warning(
                    'Change password error for %s: previous password ' +
                    'is incorrect',
                    current_user.username)
                return redirect('/change_password')

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
