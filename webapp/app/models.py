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
    accountId = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = db.relationship("Account", back_populates="profile")
    cards = db.relationship("Card", backref="profile")
    profileTickets = db.relationship("Ticket", backref="profile")

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
    nameOnCard = db.Column(db.String(250))
    billingAddress = db.Column(db.String(250))
    cardNumber = db.Column(db.Integer)
    cvc = db.Column(db.Integer)
    expiryDateMonth = db.Column(db.Integer)
    expiryDateYear = db.Column(db.Integer)
    profileId = db.Column(db.Integer, db.ForeignKey('profile.id'))

    def __repr__(self):
        return '<Card %r %r %r %r %r %r %r >' % (self.id,
                        self.nameOnCard,
                        self.billingAddress,
                        self.cardNumber,
                        self.cvc,
                        self.expiryDateMonth,
                        self.expiryDateYear
                    )


class Certificate(db.Model):
    """
    Simple table to store film certificates.

    OAPs will be '0' in table
    Adults will be '1' in table
    Students will be '2' in table
    Children will be '3' in table
    """
    __tablename__ = "certificate"

    id = db.Column(db.Integer, primary_key=True)
    cert = db.Column(db.Integer(5))
    certFilmDets = db.relationship('FilmDetails', backref='filmDetCertificate')

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
    filmName = db.Column(db.String(255))
    filmBlurb = db.Column(db.String(512))
    filmDirector = db.Column(db.String(255))
    filmActor = db.Column(db.String(255))
    filmCertificateId = db.Column(db.Integer, db.ForeignKey('certificate.id'))
    screening = db.relationship('FilmScreening', backref='filmDetScreening')

    def __repr__(self):
        return '<Film Name: %r>' % (self.id)


class FilmScreening(db.Model):
    """
    A reperesentation of a film screening consisting of a datetime and film
    detail.
    add cinema screen num
    """
    __tablename__ = 'film_screening'

    id = db.Column(db.Integer, primary_key=True)
    filmScreeningFilmDet = db.Column(db.Integer, db.ForeignKey(FilmDetails.id))
    filmScreeningTime = db.Column(DateTime)
    filmScreeningTickets = db.relationship("Ticket", backref="film_screening")
    theatreId = db.Column(db.Integer, db.ForeignKey('theatre.id'))

    def __repr__(self):
        return '<Film: %r\nScreening: %r>' % (
            self.filmScreeningTickets.filmName, self.screeningTime)


class Ticket(db.Model):
    """
    A table containing details for a ticket, including reference to its owner,
    screening, Ticket Type, and seat number

    TODO: check backrefs (they're in the Profile, TicketType, and
    FilmScreening tables) work
    """
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True)
    ownerProfileId = db.Column(db.Integer, db.ForeignKey('profile.id'))
    ticketTypeId = db.Column(db.Integer, db.ForeignKey('ticket_type.id'))
    ticketScreeningId = db.Column(db.Integer, db.ForeignKey('film_screening.id'))
    ticketDateBought = db.Column(DateTime)
    seatReserves = db.relationship('SeatReserved', backref='seatResTicket')

    def __repr__(self):
        return '<Ticket %r %r>' % (self.id, self.ticketDateBought)


class TicketType(db.Model):
    """
    Simple representation of a ticket type i.e. standard, student,
    OAP, child, etc.

    OAPs will be '0' in table
    Adults will be '1' in table
    Students will be '2' in table
    Children will be '3' in table
    """
    __tablename__ = 'ticket_type'

    id = db.Column(db.Integer, primary_key=True)
    ticketType = db.Column(db.Integer(5), unique=True)
    ticketTypeTickets = db.relationship("Ticket", backref="ticket_type")

    def __repr__(self):
        return '<Ticket Type %r>' % (self.ticketType)


class SeatReserved(db.Model):
    """
    Representation of the reserved seats.
    """
    __tablename__ = 'seat_reserved'

    id = db.Column(db.Integer, primary_key=True)
    seatId = db.Column(db.Integer, db.ForeignKey('seat.id'))
    ticketId = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    filmScreeningId = db.Column(db.Integer, db.ForeignKey('film_screening.id'))

    def __repr__(self):
        return '<Ticket Type %r>' % (self.id)


class Seat(db.Model):
    """
    Simple representation of the seats for one of the theatres.
    """
    __tablename__ = 'seat'

    id = db.Column(db.Integer, primary_key=True)
    seatPos = db.Column(db.Integer)
    theatreId = db.Column(db.Integer, db.ForeignKey('theatre.id'))
    seatSeatReserves = db.relationship('SeatReserved', backref="seat")

    def __repr__(self):
        return '<Ticket Type %r>' % (self.id)


class Theatre(db.Model):
    """
    Simple representation of the different theatres at the cinema.
    """
    __tablename__ = 'theatre'

    id = db.Column(db.Integer, primary_key=True)
    theatreName = db.Column(db.String, unique=True)
    theatreScreening = db.relationship('FilmScreening', backref='theatre')
    theatreSeat = db.relationship('Seat', backref='theatre_seat')

    def __repr__(self):
        return '<Ticket Type %r>' % (self.theatreName)


class Sales(db.Model):
    """
    A table containing details for the sales info for a film
    """
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Sales %r>' % (self.id)
