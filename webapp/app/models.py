from app import db
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash


class Account(db.Model):
    """
    Account table represents a user in the database
    The email address will be used as a representation of the account
    A staff boolean field: true if account is a staff account toerwise false

    # TODO: Hash passwords!!!
    """
    __tablename__ = 'account'

    id = db.Column(Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True)
    password = db.Column(db.String(255))
    staff = db.Column(db.Boolean)
    profile = db.relationship("Profile", uselist=False, back_populates="account")

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


class Profile(db.Model):
    """
    A representation of a customer profile.
    Each customer Profile will be associated with an Account object.
    # TODO: Check whick other columns are needed in this table
    """
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = db.relationship("Account", back_populates="profile")
    cards = db.relationship("Card", backref="profile")
    profile_tickets = db.relationship("Ticket", backref="profile")

    def __repr__(self):
        return '<Profile: %r>' % (self.surname)


class Card(db.Model):
    """
    Representation of a debit/credit card.
    All integer rows are now hashed, but cannot be unhashed. This seems
    stupid but backlog asks for user security?
    """
    __tablename__= 'card'

    id = db.Column(db.Integer, primary_key=True)
    name_on_card = db.Column(db.String(250))
    billing_address = db.Column(db.String(250))
    card_number = db.Column(db.Integer)
    cvc = db.Column(db.Integer)
    expiry_date_month = db.Column(db.Integer)
    expiry_date_year = db.Column(db.Integer)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))

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

    OAPs will be '1' in table
    Adults will be '2' in table
    Students will be '3' in table
    Children will be '4' in table
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
    of the film. screening is a backref so the film_screening table can
    reference the Film Details.
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


class FilmScreening(db.Model):
    """
    A reperesentation of a film screening consisting of a datetime and film
    detail.
    add cinema screen num
    """
    __tablename__ = 'film_screening'

    id = db.Column(db.Integer, primary_key=True)
    film_screening_film_det = db.Column(db.Integer,
                                            db.ForeignKey('film_details.id'))
    film_screening_time = db.Column(DateTime)
    film_screening_tickets = db.relationship("Ticket", backref="film_screening")
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'))

    def __repr__(self):
        return '<Film: %r\nScreening: %r>' % (
            self.film_screening_tickets.filmName, self.screening_time)


class Ticket(db.Model):
    """
    A table containing details for a ticket, including reference to its owner,
    screening, Ticket Type, and seat number

    TODO: check backrefs (they're in the Profile, TicketType, and
    FilmScreening tables) work
    """
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True)
    owner_profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    ticket_type_id = db.Column(db.Integer, db.ForeignKey('ticket_type.id'))
    ticket_screening_id = db.Column(db.Integer, db.ForeignKey('film_screening.id'))
    ticket_date_bought = db.Column(DateTime)
    seat_reserves = db.relationship('SeatReserved', backref='ticket')

    def __repr__(self):
        return '<Ticket %r %r>' % (self.id, self.ticket_date_bought)


class TicketType(db.Model):
    """
    Simple representation of a ticket type i.e. standard, student,
    OAP, child, etc.

    OAPs will be '1' in table
    Adults will be '2' in table
    Students will be '3' in table
    Children will be '4' in table
    VIP will be '5' in table

    """
    __tablename__ = 'ticket_type'

    id = db.Column(db.Integer, primary_key=True)
    ticket_type = db.Column(db.Integer)
    ticket_type_Tickets = db.relationship("Ticket", backref="ticket_type")

    def __repr__(self):
        return '<Ticket Type %r>' % (self.ticket_type)


class SeatReserved(db.Model):
    """
    Representation of the reserved seats.
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
    Simple representation of the seats for one of the theatres.
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
    """
    __tablename__ = 'theatre'

    id = db.Column(db.Integer, primary_key=True)
    theatre_name = db.Column(db.String, unique=True)
    theatre_screening = db.relationship('FilmScreening', backref='theatre')
    theatre_seat = db.relationship('Seat', backref='theatre')

    def __repr__(self):
        return '<Theatre name: %r>' % (self.theatreName)
