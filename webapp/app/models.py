from app import db
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref


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

    def __repr__(self):
        return '<User: %r>' % (self.email)


class Profile(db.Model):
    """
    A representation of a customer profile.
    Each customer Profile will be associated with an Account object.
    # TODO: Check whick other columns are needed in this table
    """
    __tablename__ = 'profile'

    account = Column(Integer, ForeignKey(Account.id), primary_key=True)
    name = Column(String(255))

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
