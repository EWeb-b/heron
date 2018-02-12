from app import db

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    forename = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    card_number = db.Column(db.Integer(16))
    cvc = db.Column(db.Integer(3))
    expiry_date = db.Column(db.Integer(4))

    def __init__(self,email,password,forename,surname,card_number,cvc,expiry_date):
        self.email = email
        self.password = password
        self.forename = forename
        self.surname = surname
        self.card_number = card_number
        self.cvc = cvc
        self.expiry_date = expiry_date

    def __repr__(self):
        return '<User %r>' % (self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return str(self.id)
