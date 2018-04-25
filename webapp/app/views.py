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
                     TicketType, Card, SeatReserved, Seat)
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

# creates a QR code from a string in /basket when a ticket is bought


def qrStringEncoder(string):
    cwd = os.getcwd()
    qrcode = pyqrcode.create(string)
    qrcode.png(cwd+'/ticketQrCode.png', scale=8)


@login_manager.user_loader
def load_user(user_id):
    return Account.query.filter(Account.id == int(user_id)).first()

# flash fields of the form that is causing the invalid form validation


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

# sends an email and qr code using the passed varaibles from the ticket
# made from /basket


@app.route('/send-mail')
def email_ticket():
    cwd = os.getcwd()
    """
    Each ticket needs to generate its own unique variable which will be passed
    to the qrStringEncoder function. This will be a combination of the
    screening, the theatre and seats and film name.
    Email also needs to include these details.
    """
    film_chosen = session.get('film_title', None)
    time = session.get('film_time', None)
    ticket_type = session.get('ticket_type', None)
    seat_number = session.get('seat_number', None)
    card_number = session.get('card_number', None)
    first_name = session.get('first_name', None)
    last_name = session.get('last_name', None)
    address = session.get('address', None)
    postcode = session.get('postcode', None)
    try:
        qrStringEncoder(film_chosen+time+ticket_type +
                        seat_number+card_number)
        msg = Message("Heron Cinema Ticket",
                      sender="movies.heron@gmail.com",
                      recipients=[current_user.email])
        # email body made using session variables from filled in information
        # from /basket
        msg.body = ("Thank you for your purchase, your ticket is attached to this email.\n\n"
                    "Customer Details: \n"
                    + first_name + " " + last_name + "\n"
                    + address + "\n"
                    + postcode + "\n\n"
                    + "Ticket details: \n"
                    + film_chosen + "\n"
                    + "Screening Time:  " + time + "\n"
                    + "Ticket Type:  " + ticket_type + "\n"
                    + "Seat Number:  " + seat_number + "\n")

        with app.open_resource(cwd+"/ticketQrCode.png") as fp:
            msg.attach("ticketQrCode", "ticketQrCode/png", fp.read())
        mail.send(msg)
        # end all sessions used to buy the ticket being sent
        session.pop('film_title')
        session.pop('film_time')
        session.pop('ticket_type')
        session.pop('seat_number')
        session.pop('card_number')
        session.pop('time')
        session.pop('film_chosen')
        session.pop('first_name')
        session.pop('last_name')
        session.pop('address')
        session.pop('postcode')
        flash("Order successfully registered")
        return redirect('/profile')

    except Exception as e:
        return str(e) + ' | email_ticket function error.'

# redirect to home


@app.route('/')
@app.route('/index')
def index():
    return redirect('/home')


@app.route('/home')
def home():
    return render_template(
        'home.html', title='Heron Home')

# logs out the current_user that started a session when logging in


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

# login for users that are stored in the database, creates a new current_user
# session


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

# creates a new user and stores them into the database, also logs them in
# and creates a new session for the user


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
                    # new user generated then stored in the database
                    newuser = Account(
                        email=form.email.data,
                        # hash the password so cannot be accessed by anyone else
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

# changes the current_users password


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
            if check_password_hash(current_user.password, form.prev_password.data):
                if form.new_password.data == form.confirmation.data:
                    current_user.password = generate_password_hash(form.new_password.data)
                    db.session.commit()
                    flash('Password changed successfully')
                    logging.info(
                        '%s successfully changed their password',
                        current_user.email)
                    return redirect('/profile')
                else:
                    flash_errors(form)
                    return redirect('/change_password')

            else:
                flash('Previous Password is incorrect')
                logging.warning(
                    'Change password error for %s: previous password ' +
                    'is incorrect',
                    current_user.email)
                return redirect('/change_password')
        else:

            flash_errors(form)
            logging.warning(
                'Change password error for %s: form validation error',
                current_user.email)
            return redirect('/change_password')

# function to add a debit card to the users account


@app.route('/add_card', methods=['GET', 'POST'])
@login_required
def add_card():
    form = CardDetails()
    if request.method == 'GET':
        return render_template(
            'add_card.html', title='Add Card', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            # If data in form was added correctly
            if (check_password_hash(current_user.password, form.password.data)):
                # If passwords match, create a new Card object with the parameters
                # enetered by the user in the form.
                newCard = Card(
                    name_on_card=form.name_on_card.data,
                    billing_address=form.billing_address.data,
                    # last_four_digits is used in /basket when user selects
                    # which they card they want to pay with.
                    last_four_digits=int(str(form.card_number.data)[12:]),
                    card_number=hashNumber(form.card_number.data),
                    cvc=hashNumber(form.cvc.data),
                    expiry_date_month=hashNumber(form.expiry_date_month.data),
                    expiry_date_year=hashNumber(form.expiry_date_year.data),
                    account_id=current_user.id
                )
                db.session.add(newCard)
                db.session.commit()
                flash('successfully added card')
                return redirect('/profile')
            else:
                flash("passwords didn't match")
                return redirect('/add_card')
        else:
            flash_errors(form)
            flash('form did not validate on submit')
            return redirect('/add_card')

# creates a ticket that is used to generate an email and QR code, all
# sessions point to here to be used to store entries in the database


@app.route('/basket', methods=['GET', 'POST'])
@login_required
def basket():
    form = Basket()
    # uses current date to be used on the ticket
    date = datetime.datetime.now()
    cards = models.Card.query.filter_by(account_id=current_user.id).all()
    # set basket to empty if the user didnt complete the website routine
    # for adding an order to the basket
    if session.get('seat_number') is None:
        film_chosen = None
        time = None
    else:
        film_chosen = session.get('film_chosen', None)
        time = session.get('time', 'N/A')
    ticket_type = session.get('ticket_type', 'N/A')
    seat_number = session.get('seat_number', None)
    theatre_id = session.get('theatre', None)
    screening_id = session.get('screening_id', None)

    # check what ticket type the ticket should be using both the seat chosen
    # and the ticket type chosen in /order_ticket
    if session.get('seat_number') is not None:
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
    if not cards:
        choices = [("No Saved Cards", "No Saved Cards")]
    else:
        choices = [(str(i.last_four_digits), str(i.last_four_digits)) for i in cards]
    form.card.choices = choices

    # if-else statements to find the value the ticket should be
    if film_chosen == None:
        ticket_value = 0
    else:
        if session.get('seat_number') is not None:
            if (int(seat_number) == 9 or int(seat_number) == 10 or
                    int(seat_number) == 11 or int(seat_number) == 12 or
                    int(seat_number) == 13 or int(seat_number) == 14 or
                    int(seat_number) == 15 or int(seat_number) == 16):
                ticket_value = 6
            elif ticket_type == 'standard':
                ticket_value = 5
            else:
                ticket_value = 4
        else:
            ticket_value = 0

    if request.method == 'GET':
        return render_template(
            'basket.html', title='Checkout', ticket_film=film_chosen,
            ticket_value=ticket_value, film_time=time,
            ticket_type=ticket_type, seat_number=seat_number, cards=cards,
            form=form)
    elif request.method == 'POST':
        print('posting')
        if film_chosen != None:
            if form.validate() == True:
                print('validation successful')
                # generate sessions for user info to be used in the ticket email
                session['card_number'] = form.card.data
                session['first_name'] = form.first_name.data
                session['last_name'] = form.last_name.data
                session['address'] = form.address.data
                session['postcode'] = form.postcode.data
                # store a ticket into the database
                newTicket = Ticket(
                    owner_account_id=current_user.id,
                    ticket_type_id=ticket_type_number,
                    ticket_date_bought=date,
                )
                db.session.add(newTicket)
                db.session.commit()
                newReserveSeat = SeatReserved(ticket_id=newTicket.id)
                db.session.add(newReserveSeat)
                db.session.commit()
                # send the ticket using /send-email
                return redirect('/send-mail')
            else:
                flash_errors(form)
                return redirect('/basket')
        else:
            flash('No film in basket')
            return redirect('/basket')


@app.route('/order_ticket', methods=['GET', 'POST'])
def order_ticket():
    if session.get('seat_number') is not None:
        # remove sessions for seat number and ticket type if the user
        # attempts to buy a new ticket with a different film
        session.pop('seat_number')
        session.pop('ticket_type')
    form = OrderTicket()
    ticket_type = session.get('ticket_type', 'N/A')
    film_time = session.get('film_time', 'N/A')
    film_title = session.get('film_title', None)
    film = models.FilmDetails.query.filter_by(film_name=film_title).first_or_404()

    if request.method == 'GET':
        return render_template(
            'order_ticket.html', title='Order Ticket', form=form, film=film)

    elif request.method == 'POST':
        print('posting')
        if form.validate() == True:
            print('validation successful')
            session['film_chosen'] = film_title
            session['time'] = film_time
            session['seat_number'] = form.seat_number.data
            session['ticket_type'] = form.ticket_type.data
            return redirect('/basket')
        else:
            print('Fail')
            flash_errors(form)
            return redirect('/order_ticket')

# page that shows the film information as well as the trailer for the film
# the function queries the databse to check what screening times are available
# the chosen film today


@app.route('/film_info', methods=['GET', 'POST'])
def film_details():
    form = ShowTimes()
    passed = request.args.get('passed', None)
    film = models.FilmDetails.query.filter_by(film_name=passed).first_or_404()
    # query to find the available screening times
    film_times = FilmScreening.query.join(FilmDetails).filter(FilmScreening.film_screening_film_det == film.id, FilmScreening.film_screening_time.between(
        datetime.date.today(), datetime.date.today() + datetime.timedelta(1))).all()
    # query to find which theatre the film is showing in
    theatre = models.FilmScreening.query.with_entities(FilmScreening.theatre_id).filter(
        FilmScreening.film_screening_film_det == film.id).first()
    # find the screening id for the specific screening time and theatre
    screening_id = FilmScreening.query.with_entities(FilmScreening.id).join(FilmDetails).filter(FilmScreening.film_screening_film_det == film.id, FilmScreening.film_screening_time.between(
        datetime.date.today(), datetime.date.today() + datetime.timedelta(1))).all()

    times = []
    # convert the datetimes returned into the 24 hour clock to be used as an
    # option in the SelectField on the webpage
    for showing in film_times:
        time = showing.film_screening_time
        times.append(str(time.hour) + ":" + "{:02d}".format(time.minute))
    print(times)

    if not times:
        choices = [("No Screening Times Available", "No Screening Times Available")]
    else:
        choices = [(i, i) for i in times]
    form.time.choices = choices

    if request.method == 'GET':
        return render_template(
            'filmInfo.html', title='Film Details', times=times, film=film, passed=passed, form=form)
    elif request.method == 'POST':
        if form.validate() == True:
            print('validation successful')
            session['screening_id'] = screening_id
            session['theatre'] = theatre
            session['film_title'] = passed
            session['film_time'] = form.time.data
            return redirect('/order_ticket')
        else:
            flash_errors(form)
            return render_template(
                'filmInfo.html', title='Film Details', film=film, passed=passed, form=form)

# list all the films currently showing at the cinema


@app.route('/film_details', methods=['GET', 'POST'])
def list_films():
    # print list of films stored in FilmDetails databse
    filmDetails = models.FilmDetails.query.all()
    # userList = models.Account.query.all()
    return render_template(
        'filmDetails.html', title='Film List', filmDetails=filmDetails)

# shows the debit cards stored and the ticket history of the user


@app.route('/profile', methods=['GET'])
@login_required
def profile():

    cards = Card.query.filter_by(account_id=current_user.id).all()
    tickets = Ticket.query.join(Account).join(FilmScreening).join(
        FilmDetails).filter(Ticket.owner_account_id == current_user.id).all()

    return render_template(
        'profile.html', title='User Profile', cards=cards, tickets=tickets)


@app.route('/screenings', methods=['GET'])
def screenings():

    films_of_the_day = FilmDetails.query.limit(3).all()

    return render_template(
        'screenings.html', title='Screenings', film=films_of_the_day)
