from app import db
import sqlalchemy


class Account(db.Model):
    """
    Account table represents a user in the database
    The email address will be used as a representation of the account
    A staff boolean field: true if account is a staff account toerwise false

    # TODO: Hash passwords!!!
    """
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True)
    password = db.Column(db.String(255))
    staff = db.Column(db.Boolean)

    def __repr__(self):
        return '<User: %r>' %(self.email)


class Profile(db.Model):
    """
    A representation of a customer profile.
    Each customer Profile will be associated with an Account object.
    # TODO: Check whick other columns are needed in this table
    """
    __tablename__ = 'profile'

    account = db.Column(db.Integer, ForeignKey(Account.id), primary_key=True)
    name = sb.Column(db.String(255))

    def __repr__(self):
        return '<Profile: %r>' % (self.name)


class Certificate(db.Model):
    """
    Simple table to store film certificates
    """
    __tablename__ = "certificate"

    id = db.Column(db.Integer, primary_key=True)
    cert = db.Column(db.String(4), unique=True)

    def __repr__(self):
        return '<Certificate: %r>' % (self.cert)


class FilmDetails(db.Model):
    """
    A representation of a film. Contains movie name, short description(blurb),
    the director of the film, the lead actor of the film and the certificate
    of the film
    """
    __tablename__ = 'film_details'

    id = db.Column(db.Integer, primary_key=True)
    filmName = db.Column(db.String(255))
    filmBlurb = db.Column(db.String(512))
    filmDirector = db.Column(db.String(255))
    filmActor = db.Column(db.String(255))
    filmCertificate = db.Column(db.Integer, ForeignKey(Certificate.id))

    def __repr__(self):
        return '<Film Name: %r>' % (self.filmName) 

# from sqlalchemy.inspection import inspect


# class Serializer(object):
#     """
#     A class used to aid conversion of database models into JSON
#     Adapted from StackExchange:
#     https://stackoverflow.com/a/27951648
#     """

#     def serialize(self):
#         """
#         Reads the keys from the db table and iterates over them
#         adding the data as the value.
#         """
#         return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

#     @staticmethod
#     def serializeList(items):
#         """Takes a db query that contains multiple items and serializes them.

#         Arguments:
#             items {A list containing multiple objects from a db query.}
#         """
#         return [item.serialize() for item in items]


# class UserInfo(db.Model):

#     __tablename__ = 'userinfo'

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     forename = db.Column(db.String(100))
#     surname = db.Column(db.String(100))
#     date_of_birth = db.Column(db.Date)
#     card_number = db.Column(db.Integer)
#     cvc = db.Column(db.Integer)
#     expiry_date = db.Column(db.Integer)

#     # __init__ is not needed whden using SQL-Alchemy...
#     # It's all automatic.
#     # def __init__(
#     #         self, email, password, forename,
#     #         surname, date_of_birth, card_number, cvc, expiry_date):
#     #     self.email = email
#     #     self.password = password
#     #     self.forename = forename
#     #     self.surname = surname
#     #     self.date_of_birth = date_of_birth
#     #     self.card_number = card_number
#     #     self.cvc = cvc
#     #     self.expiry_date = expiry_date

#     def __repr__(self):
#         return '<User: %r>' % (self.email)

#     def is_authenticated(self):
#         return True

#     def is_active(self):
#         return True

#     def is_anonymous(self):
#         return True

#     def get_id(self):
#         return str(self.email)


# class FilmDetails(db.Model, Serializer):

#     __tablename__ = 'film_details'

#     id = db.Column(db.Integer, primary_key=True)
#     film_name = db.Column(db.String(100))
#     blurb = db.Column(db.String(1000))
#     age_certificate = db.Column(db.Integer)
#     director = db.Column(db.String(100))
#     lead_actor = db.Column(db.String(100))

#     # def __init__(
#     #         self, film_name, blurb,
#     #         age_certificate, director, lead_actor):
#     #     self.film_name = film_name
#     #     self.blurb = blurb
#     #     self.age_certificate = age_certificate
#     #     self.director = director
#     #     self.lead_actor = lead_actor

#     def __repr__(self):
#         return '<Film: %r>' % (self.film_name)

#     def serialize(self):
#         item = Serializer.serialize(self)
#         return item


# class FilmScreenings(db.Model):

#     __tablename__ = 'film_screenings'

#     id = db.Column(db.Integer, primary_key=True)
#     film_name = db.Column(db.String(100))
#     screening_date = db.Column(db.Date)
#     screening_time = db.Column(db.Time)
#     standard_seats = db.Column(db.Integer)
#     vip_seats = db.Column(db.Integer)
#     standard_ticket = db.Column(db.Float)
#     oap_ticket = db.Column(db.Float)
#     child_ticket = db.Column(db.Float)

#     # def __init__(
#     #         self, film_name, date, screening_date, standard_seats,
#     #         vip_seats, standard_ticket, oap_ticket, child_ticket):
#     #     self.film_name = film_name
#     #     self.date = date
#     #     self.screening_time = screening_time
#     #     self.standard_seats = standard_seats
#     #     self.vip_seats = vip_seats
#     #     self.standard_ticket = standard_ticket
#     #     self.oap_ticket = oap_ticket
#     #     self.child_ticket = child_ticket

#     def __repr__(self):
#         return '<Film: %r>' % (self.film_name)
