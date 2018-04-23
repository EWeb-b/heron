import os
from flask import (
    render_template, flash, redirect, request, Flask, url_for,
    make_response, session)
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap
from app import app, db, models, mail
from .forms import (CreateAccountForm, ChangePasswordForm, LogInForm,
                    CardDetails, OrderTicket, ShowTimes, Basket)
from .models import (Account, Certificate, FilmDetails, FilmScreening, Ticket,
                     TicketType, Card)
from flask_login import (
    LoginManager, login_user, logout_user, login_required, current_user)
import datetime
import hashlib
import logging
import pyqrcode
from werkzeug.security import generate_password_hash, check_password_hash


# For sending emails
mail.init_app(app)


# For logging to website.log file
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


def qrStringEncoder(string):
    cwd = os.getcwd()
    print(cwd)
    qrcode = pyqrcode.create(string)
    qrcode.png(cwd+'/ticketQrCode.png', scale=8)
    print(qrcode.terminal(quiet_zone=1))


@login_manager.user_loader
def load_user(user_id):
    return Account.query.filter(Account.id == int(user_id)).first()


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.route('/send-mail')
def email_ticket():
    cwd = os.getcwd()
    """
    Each ticket needs to generate its own unique variable which will be passed
    to the qrStringEncoder function. This will be a combination of the
    screening, the theatre and seats and film name.
    Email also needs to include these details.
    """
    film_title = session.get('film_title', None)
    film_time = session.get('film_time', None)
    ticket_type = session.get('ticket_type', None)
    seat_number = session.get('seat_number', None)
    card_number = session.get('card_number', None)
    try:
        qrStringEncoder(film_title+film_time+ticket_type +
                        seat_number+card_number)
        msg = Message("Heron Cinema Ticket",
                      sender="movies.heron@gmail.com",
                      recipients=[current_user.email])
        msg.body = ("Thank you for your purchase, your ticket is attached to this email.\n\n"
                    "Ticket details: \n"
                    + film_title + "\n"
                    + "Screening Time:  " + film_time + "\n"
                    + "Ticket Type:  " + ticket_type + "\n"
                    + "Seat Number:  " + seat_number + "\n")

        with app.open_resource(cwd+"/ticketQrCode.png") as fp:
            msg.attach("ticketQrCode", "ticketQrCode/png", fp.read())
        mail.send(msg)
        session.pop('film_title')
        session.pop('film_time')
        session.pop('ticket_type')
        session.pop('seat_number')
        session.pop('card_number')
        flash("Order successfully registered")
        return redirect('/profile')

    except Exception as e:
        return str(e) + ' | email_ticket function error.'


@app.route('/')
@app.route('/index')
def index():
    return redirect('/home')


@app.route('/home')
def home():
    return render_template(
        'home.html', title='Heron Home')


@app.route('/logout')
@login_required
def logout():
    # need the name variable otherwise logging does not work
    name_email = current_user.email
    logout_user()
    session.clear()
    logging.info('User %s logged out', name_email)
    flash("Logged out successfully")
    logging.info('%s logged out successfully', name_email)
    return redirect('/login')


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
                flash("An account has already been registered with that email")
                return redirect('/create_account')
            else:
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
            flash("Error creating your account. Invalid email.")
            # logging.info()
            return redirect('/create_account')


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
                    card_number=form.card_number.data,
                    cvc=hashNumber(form.cvc.data),
                    expiry_date_month=hashNumber(form.expiry_date_month.data),
                    expiry_date_year=hashNumber(form.expiry_date_year.data),
                    account_id=current_user.id
                )
                print('card created not added')
                db.session.add(newCard)
                db.session.commit()
                flash('successfully added card')
                return redirect('/profile')
            else:
                flash("passwords didn't match")
                print("passwords didn't match")
                return redirect('/add_card')
        else:
            flash_errors(form)
            flash('form did not validate on submit')
            print('form didnt validate on submit')
            return redirect('/add_card')


@app.route('/basket', methods=['GET', 'POST'])
@login_required
def basket():
    form = Basket()
    date = datetime.datetime.now()
    print(date)
    cards = models.Card.query.filter_by(account_id=current_user.id).all()
    print(cards)
    form.card.choices = cards
    film_title = session.get('film_title', None)
    film_time = session.get('film_time', 'N/A')
    ticket_type = session.get('ticket_type', 'N/A')
    seat_number = session.get('seat_number', None)
    print(int(seat_number))

    if (int(seat_number) == 9 or int(seat_number) == 10 or
            int(seat_number) == 11 or int(seat_number) == 12 or
            int(seat_number) == 13 or int(seat_number) == 14 or
            int(seat_number) == 15 or int(seat_number) == 16):
        ticket_type_number = 5
    elif ticket_type == 'oap':
        ticket_type_number = 1
    elif ticket_type == 'standard':
        ticket_type_number = 2
    elif ticket_type == 'student':
        ticket_type_number = 3
    elif ticket_type == 'child':
        ticket_type_number = 4

    choices = [(str(i.card_number), str(i.card_number)) for i in cards]
    form.card.choices = choices

    if film_title == None:
        ticket_value = 0
    else:
        if (int(seat_number) == 9 or int(seat_number) == 10 or
                int(seat_number) == 11 or int(seat_number) == 12 or
                int(seat_number) == 13 or int(seat_number) == 14 or
                int(seat_number) == 15 or int(seat_number) == 16):
            ticket_value = 6
        elif ticket_type == 'standard':
            ticket_value = 5
        else:
            ticket_value = 4

    if request.method == 'GET':
        return render_template(
            'basket.html', title='Checkout', ticket_film=film_title,
            ticket_value=ticket_value, film_time=film_time,
            ticket_type=ticket_type, seat_number=seat_number, cards=cards,
            form=form)
    elif request.method == 'POST':
        print('posting')
        if film_title != None:
            if form.validate() == True:
                print('validation successful')
                session['card_number'] = form.card.data
                newTicket = Ticket(
                    owner_account_id=current_user.id,
                    ticket_type_id=ticket_type_number,
                    ticket_date_bought=date,
                )
                ticket = models.Ticket.query.all()
                print(ticket)
                return redirect('/send-mail')
            else:
                print('fail')
                flash_errors(form)
                return redirect('/basket')
        else:
            flash('No film in basket')
            return redirect('/basket')


@app.route('/order_ticket', methods=['GET', 'POST'])
def order_ticket():
    form = OrderTicket()
    film_title = session.get('film_title', None)
    film = models.FilmDetails.query.filter_by(film_name=film_title).first_or_404()

    if request.method == 'GET':
        return render_template(
            'order_ticket.html', title='Order Ticket', form=form, film=film)

    elif request.method == 'POST':
        print('posting')
        if form.validate() == True:
            print('validation successful')
            session['seat_number'] = form.seat_number.data
            session['ticket_type'] = form.ticket_type.data
            return redirect('/basket')
        else:
            print('Fail')
            flash_errors(form)
            return redirect('/order_ticket')


@app.route('/film_info', methods=['GET', 'POST'])
def film_details():
    form = ShowTimes()
    passed = request.args.get('passed', None)
    film = models.FilmDetails.query.filter_by(film_name=passed).first_or_404()

    if request.method == 'GET':
        return render_template(
            'filmInfo.html', title='Film Details', film=film, passed=passed, form=form)
    elif request.method == 'POST':
        if form.validate() == True:
            print('validation successful')
            session['film_title'] = passed
            session['film_time'] = form.times.data
            return redirect('/order_ticket')
        else:
            flash_errors(form)
            return render_template(
                'filmInfo.html', title='Film Details', film=film, passed=passed, form=form)


@app.route('/film_details', methods=['GET', 'POST'])
def list_films():
    # print list of films stored in FilmDetails databse
    filmDetails = models.FilmDetails.query.all()
    # userList = models.Account.query.all()
    return render_template(
        'filmDetails.html', title='Film List', filmDetails=filmDetails)


@app.route('/profile', methods=['GET'])
@login_required
def profile():
    # Return the tickets that the account owns.
    #ticketsOwned = models.Account.account_tickets.query.all()

    return render_template(
        'profile.html', title='User Profile')

@app.route('/screenings', methods=['GET'])
@login_required
def screenings():
    # Return the tickets that the account owns.
    #ticketsOwned = models.Account.account_tickets.query.all()

    return render_template(
        'screenings.html', title='Screenings')
