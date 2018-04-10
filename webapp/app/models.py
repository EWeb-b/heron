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
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship("Account", back_populates="profile")
    cards = relationship('Card')

    def __repr__(self):
        return '<Profile: %r>' % (self.name)


class Certificate(db.Model):
    """
    Simple table to store film certificates
    """
    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True)
    cert = Column(String(4), unique=True)

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
    filmCertificate = Column(Integer, ForeignKey(Certificate.id))
    screening = relationship('FilmScreening', backref='film')

    def __repr__(self):
        return '<Film Name: %r>' % (self.filmName)


class FilmScreening(db.Model):
    """
    A reperesentation of a film screening consisting of a datetime and film
    detail.
    """
    __tablename__ = 'film_screening'

    id = Column(Integer, primary_key=True)
    screeningFilm = Column(Integer, ForeignKey(FilmDetails.id))
    screeningTime = Column(DateTime)

    def __repr__(self):
        return '<Film: %r\nScreening: %r>' % (
            self.film.filmName, self.screeningTime)


class TicketType(db.Model):
    """
    Simple representation of a ticket type i.e. standard, student,
    OAP, child, etc.
    """
    __tablename__ = 'ticket_type'

    id = Column(Integer, primary_key=True)
    ticketType = Column(String(16), unique=True)

    def __repr__(self):
        return '<Ticket Type %r>' % (self.ticketType)

class Card(db.Model):
    """
    Representation of a debit/credit card.
    All integer rows are now hashed, but cannot be unhashed. This seems
    stupid but backlog asks for user security?
    """
    __tablename__= 'card'

    id = Column(Integer, primary_key=True)
    name_on_card = Column(String(250))
    billing_address = Column(String(250))
    card_number = Column(Integer)
    cvc = Column(Integer)
    expiry_date_month = Column(Integer)
    expiry_date_year = Column(Integer)
    profile_id = Column(Integer, ForeignKey('profile.id'))

    def __repr__(self):
        return '<Card %r>' % (self.id,
                        self.name_on_card,
                        self.billing_address,
                        self.card_number,
                        self.cvc,
                        self.expiry_date_month,
                        self.expiry_date_year
                    )

class Ticket(db.Model):
    """
    A table containing details for a ticket, including reference to a
    screening, Ticket Type, and seat number
    
    Possible TODO: add backrefs? not sure if needed
    """
    __tablename__ = 'ticket'
    
    id = Column(Integer, primary_key=True)
    ticketType = Column(Integer, ForeignKey('TicketType.id'))
    ticketScreening = Column(Integer, ForeignKey('FilmScreening.id'))
    ticketSeatNumber = Column(Integer)
    
    def __repr__(self):
        return 'Ticket %r>' % (self.id)
