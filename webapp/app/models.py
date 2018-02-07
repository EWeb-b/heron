class UserInfo(db.Model):

    __tablename__ = 'userinfo'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    forename = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    card_number = db.Column(db.Integer)
    cvc = db.Column(db.Integer)
    expiry_date = db.Column(db.Integer)

    def __init__(self,email,password,forename,surname,card_number,cvc,expiry_date):
        self.email = email
        self.password = password
        self.forename = forename
        self.surname = surname
        self.card_number = card_number
        self.cvc = cvc
        self.expiry_date = expiry_date

    def __repr__(self):
        return '<User: %r>' % (self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return str(self.email)



class FilmDetails(db.Model):

    __tablename__ = 'film_details'

    id = db.Column(db.Integer, primary_key=True)
    film_name = db.Column(db.String(100))
    blurb = db.Column(db.String(1000))
    age_certificate = db.Column(db.Integer)
    director = db.Column(db.String(100))
    lead_actor = db.Column(db.String(100))

    def __init__(self,film_name,blurb,age_certificate,director,lead_actor):
        self.film_name = film_name
        self.blurb = blurb
        self.age_certificate = age_certificate
        self.director = director
        self.lead_actor = lead_actor

    def __repr__(self):
        return '<Film: %r>' % (self.film_name)



class FilmScreenings(db.Model):

    __tablename__ = 'film_screenings'

    id = db.Column(db.Integer, primary_key=True)
    film_name = db.Column(db.String(100))
    screening_date = db.Column(db.Date)
    screening_time = db.Column(db.Time)
    standard_seats = db.Column(db.Integer)
    vip_seats = db.Column(db.Integer)
    standard_ticket = db.Column(db.Float)
    oap_ticket = db.Column(db.Float)
    child_ticket = db.Column(db.Float)

    def __init__(self,film_name,date,screening_date,standard_seats,vip_seats,standard_ticket,oap_ticket,child_ticket):
        self.film_name = film_name
        self.date = date
        self.screening_time = screening_time
        self.standard_seats = standard_seats
        self.vip_seats = vip_seats
        self.standard_ticket = standard_ticket
        self.oap_ticket = oap_ticket
        self.child_ticket = child_ticket

    def __repr__(self):
        return '<Film: %r>' % (self.film_name)
