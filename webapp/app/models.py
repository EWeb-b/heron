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

    id = Column(Integer, primary_key=True)
    email = Column(String(254), unique=True)
    password = Column(String(255))
    staff = Column(Boolean)
    profile = relationship("Profile", uselist=False, back_populates="account")

    def __repr__(self):
        return '<User: %r>' % (self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return true

    def is_anonymous(self):
        return false

    def get_id(self):
        return str(self.id)


class Profile(db.Model):
    """
    A representation of a customer profile.
    Each customer Profile will be associated with an Account object.
    # TODO: Check whick other columns are needed in this table
    """
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    forename = Column(String(255))
    surname = Column(String(255))
    accountId = Column(Integer, ForeignKey('account.id'))
    account = relationship("Account", back_populates="profile")
    cards = relationship("Card", backref="profile")
    profileTickets = relationship("Ticket", backref="profile")

    def __repr__(self):
        return '<Profile: %r>' % (self.name)


class Card(db.Model):
    """
    Representation of a debit/credit card.
    All integer rows are now hashed, but cannot be unhashed. This seems
    stupid but backlog asks for user security?
    """
    __tablename__= 'card'

    id = Column(Integer, primary_key=True)
    nameOnCard = Column(String(250))
    billingAddress = Column(String(250))
    cardNumber = Column(Integer)
    cvc = Column(Integer)
    expiryDateMonth = Column(Integer)
    expiryDateYear = Column(Integer)
    profileId = Column(Integer, ForeignKey('profile.id'))

    def __repr__(self):
        return '<Card %r>' % (self.id,
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

    OAPs will be 'oap' in table
    Adults will be 'adult' in table
    Students will be 'stud' in table
    Children will be 'child' in table
    """
    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True)
    cert = Column(String(5), unique=True)
    certFilmDets = relationship('Ticket', backref='filmDetCertificate')

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

    id = Column(Integer, primary_key=True)
    filmName = Column(String(255))
    filmBlurb = Column(String(512))
    filmDirector = Column(String(255))
    filmActor = Column(String(255))
    filmCertificateId = Column(Integer, ForeignKey(Certificate.id))
    screening = relationship('FilmScreening', backref='filmDetScreening')

    def __repr__(self):
        return '<Film Name: %r>' % (self.filmName)


class FilmScreening(db.Model):
    """
    A reperesentation of a film screening consisting of a datetime and film
    detail.
    add cinema screen num
    """
    __tablename__ = 'film_screening'

    id = Column(Integer, primary_key=True)
    filmScreeningFilmDet = Column(Integer, ForeignKey(FilmDetails.id))
    filmScreeningTime = Column(DateTime)
    filmScreeningTickets = relationship("Ticket", backref="film_screening")

    def __repr__(self):
        return '<Film: %r\nScreening: %r>' % (
            self.film.filmName, self.screeningTime)


class Ticket(db.Model):
    """
    A table containing details for a ticket, including reference to its owner,
    screening, Ticket Type, and seat number

    TODO: check backrefs (they're in the Profile, TicketType, and
    FilmScreening tables) work
    """
    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True)
    ownerProfileId = Column(Integer, ForeignKey('profile.id'))
    ticketTypeId = Column(Integer, ForeignKey('ticket_type.id'))
    ticketScreeningId = Column(Integer, ForeignKey('film_screening.id'))
    ticketDateBought = Column(DateTime)
    seatReserves = relationship('SeatReserved', backref='seatResTicket')

    def __repr__(self):
        return 'Ticket %r>' % (self.id)


class TicketType(db.Model):
    """
    Simple representation of a ticket type i.e. standard, student,
    OAP, child, etc.

    OAPs will be 'oap' in table
    Adults will be 'adult' in table
    Students will be 'stud' in table
    Children will be 'child' in table
    """
    __tablename__ = 'ticket_type'

    id = Column(Integer, primary_key=True)
    ticketType = Column(String(5), unique=True)
    ticketTypeTickets = relationship("Ticket", backref="ticket_type")

    def __repr__(self):
        return '<Ticket Type %r>' % (self.ticketType)


class SeatReserved(db.Model):
    """
    Representation of the reserved seats.
    """
    __tablename__ = 'seat_reserved'

    id = Column(Integer, primary_key=True)
    seatId = Column(Integer, ForeignKey('seat.id'))
    ticketId = Column(Integer, ForeignKey('ticket.id'))
    filmScreeningId = Column(Integer, ForeignKey('film_screening.id'))

    def __repr__(self):
        return '<Ticket Type %r>' % (self.id)


class Seat(db.Model):
    """
    Simple representation of the seats for one of the theatres.
    """
    __tablename__ = 'seat'

    id = Column(Integer, primary_key=True)
    seatPos = Column(Integer)
    theatreId = Column(Integer, ForeignKey('theatre.id'))
    seatSeatReserves = relationship('SeatReserved', backref="seat")

    def __repr__(self):
        return '<Ticket Type %r>' % (self.id)


class Theatre(db.Model):
    """
    Simple representation of the different theatres at the cinema.
    """
    __tablename__ = 'theatre'

    id = Column(Integer, primary_key=True)
    theatreName = Column(String, unique=True)
    theatreScreening = relationship('FilmScreening', backref='theatre')
    theatreSeat = relationship('Seat', backref='theatre_seat')

    def __repr__(self):
        return '<Ticket Type %r>' % (self.theatreName)


class Sales(db.Model):
    """
    A table containing details for the sales info for a film
    """
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return '<Sales %r>' % (self.id)
