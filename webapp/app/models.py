from app import db
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash


class Account(db.Model):
    """
    Account table represents a user in the database
    The email address will be used as a representation of the account
    A staff boolean field: true if account is a staff account otherwise false.

    Relationships:
        One Account to many Cards
        One Account to many Tickets
    """
    __tablename__ = 'account'

    id = db.Column(Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True)
    password = db.Column(db.String(255))
    staff = db.Column(db.Boolean)
    cards = db.relationship("Card", backref="account")
    account_tickets = db.relationship("Ticket", backref="account")

    def __repr__(self):
        return '<User: %r>' % (self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Card(db.Model):
    """
    Representation of a debit/credit card.
    card_number and some other columns are of type String because the hash
    function in views.py returns a string.

    Relationships:
        Many Cards to one Account
    """
    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)
    name_on_card = db.Column(db.String(250))
    billing_address = db.Column(db.String(250))
    last_four_digits = db.Column(db.Integer)
    card_number = db.Column(db.String)
    cvc = db.Column(db.String)
    expiry_date_month = db.Column(db.String)
    expiry_date_year = db.Column(db.String)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __repr__(self):
        return '<Card %r %r %r %r %r %r %r >' % (self.id,
                                                 self.name_on_card,
                                                 self.billing_address,
                                                 self.card_number,
                                                 self.cvc,
                                                 self.expiry_date_month,
                                                 self.expiry_date_year
                                                 )


class Certificate(db.Model):
    """
    Simple table to store film certificates.

    U will be '1' in table
    PG will be '2' in table
    12 will be '3' in table
    15 will be '4' in table
    18 will be '5' in table

    Relationships:
        One Certificate to many FilmDetails
    """
    __tablename__ = "certificate"

    id = db.Column(db.Integer, primary_key=True)
    cert = db.Column(db.Integer)
    cert_film_dets = db.relationship('FilmDetails', backref='certificate')

    def __repr__(self):
        return '<Certificate: %r>' % (self.cert)


class FilmDetails(db.Model):
    """
    A representation of a film. Contains movie name, short description(blurb),
    the director of the film, the lead actor of the film and the certificate
    of the film.

    Relationships:
        Many FilmDetails to one Certificate
        One FilmDetails to many FilmScreenings
    """
    __tablename__ = 'film_details'

    id = db.Column(db.Integer, primary_key=True)
    film_name = db.Column(db.String(255))
    film_blurb = db.Column(db.String(512))
    film_director = db.Column(db.String(255))
    film_actor = db.Column(db.String(255))
    film_certificate_id = db.Column(db.Integer, db.ForeignKey('certificate.id'))
    screening = db.relationship('FilmScreening', backref='film_details')

    def __repr__(self):
        return '<Film Name: %r>' % (self.film_name)

    def __json__(self):
        return ['id', 'film_name', 'film_blurb', 'film_director',
                'film_actor', 'film_certificate_id']


class FilmScreening(db.Model):
    """
    A reperesentation of a film screening consisting of a datetime.
    Includes references to FilmDetails, SeatReserved, Ticket, and Theatre

    Relationships:
        One FilmScreening to many Tickets
        One FilmScreening to many SeatReserved
        Many FilmScreenings to one FilmDetails
        Many FilmScreenings to one Theatre
    """
    __tablename__ = 'film_screening'

    id = db.Column(db.Integer, primary_key=True)
    film_screening_film_det = db.Column(db.Integer,
                                        db.ForeignKey('film_details.id'))
    film_screening_time = db.Column(DateTime)
    film_screening_tickets = db.relationship("Ticket", backref="film_screening")
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'))

    def __repr__(self):
        return '''<id: %r, film_details_id: %r, screening_time: %r,
        theatre_id: %r\n>''' % (self.id, self.film_screening_film_det,
                                self.film_screening_time, self.theatre_id)

    def __json__(self):
        return ['id', 'film_screening_film_det', 'film_screening_time', 'theatre_id']


class Ticket(db.Model):
    """
    A table containing details for a ticket, including reference to its owner,
    screening, Ticket Type, and seat number

    Relationships:
        One Ticket to many SeatReserved
        Many Tickets to one Account
        Many Tickets to one FilmScreening
        Many Tickets to one TicketType
    """
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True)
    owner_account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    ticket_type_id = db.Column(db.Integer, db.ForeignKey('ticket_type.id'))
    ticket_screening_id = db.Column(db.Integer, db.ForeignKey('film_screening.id'))
    ticket_date_bought = db.Column(DateTime)
    seat_reserves = db.relationship('SeatReserved', backref='ticket')

    def __repr__(self):
        return '''<ticket_id: %r, owner_account_id: %r, ticket_type_id: %r,
         ticket_screening_id: %r, ticket_date_bought: %r>''' % (self.id,
                                                                self.owner_account_id,
                                                                self.ticket_type_id,
                                                                self.ticket_screening_id,
                                                                self.ticket_date_bought
                                                                )

    def __json__(self):
        return ['id', 'owner_account_id', 'ticket_type_id', 'ticket_screening_id',
                'ticket_date_bought']


class TicketType(db.Model):
    """
    Simple representation of a ticket type i.e. standard, student,
    OAP, child, etc.

    OAP ticket will be '1' in table
    Standard ticket will be '2' in table
    Student ticket will be '3' in table
    Child ticket will be '4' in table
    VIP ticket will be '5' in table

    Relationships:
        One TicketType to many Tickets
    """
    __tablename__ = 'ticket_type'

    id = db.Column(db.Integer, primary_key=True)
    ticket_type = db.Column(db.Integer)
    ticket_type_Tickets = db.relationship("Ticket", backref="ticket_type")

    def __repr__(self):
        return '<Ticket Type %r>' % (self.ticket_type)


class SeatReserved(db.Model):
    """
    Representation of the reserved seats for a particular FilmScreening

    Relationships:
        Many SeatReserved to one Ticket
        Many SeatReserved to one FilmScreening
        Many SeatReserved to one Seat
    """
    __tablename__ = 'seat_reserved'

    id = db.Column(db.Integer, primary_key=True)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    film_screening_id = db.Column(db.Integer, db.ForeignKey('film_screening.id'))

    def __repr__(self):
        return '<Ticket Type %r>' % (self.id)


class Seat(db.Model):
    """
    Simple representation of the seats for a particular Theatre

    Relationships:
        One Seat to many SeatReserved
        Many Seats to one Theatre
    """
    __tablename__ = 'seat'

    id = db.Column(db.Integer, primary_key=True)
    seat_pos = db.Column(db.Integer)
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'))
    seat_seat_reserves = db.relationship('SeatReserved', backref="seat")

    def __repr__(self):
        return '<Theatre id, seat no.: %r %r>' % (self.theatre_id, self.seat_pos)


class Theatre(db.Model):
    """
    Simple representation of the different theatres at the cinema.

    Relationships:
        One Theatre to many Seats
        One Theatre to many FilmScreenings
    """
    __tablename__ = 'theatre'

    id = db.Column(db.Integer, primary_key=True)
    theatre_name = db.Column(db.String, unique=True)
    theatre_screening = db.relationship('FilmScreening', backref='theatre')
    theatre_seat = db.relationship('Seat', backref='theatre')

    def __repr__(self):
        return '<Theatre name: %r>' % (self.theatre_name)
