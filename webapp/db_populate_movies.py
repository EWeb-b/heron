from flask import Flask
from app.models import (FilmDetails, Ticket, Seat, Theatre, Certificate,
                        TicketType, FilmScreening, Account, Card)
from app import app, db, models
from datetime import datetime
from calendar import monthrange
from random import randint
import json
from werkzeug.security import generate_password_hash, check_password_hash


################################################################################

# Populates the FilmDetails table with films.
# Certificates 1=U , 2=PG, 3=12, 4=15, 5=18.

filmData = [
    {
        "id": 1,
        "film_certificate_id": 3,
        "film_blurb": """A thief, who steals corporate secrets through the use
                        of dream-sharing technology, is given the inverse task
                        of planting an idea into the mind of a CEO.""",
        "film_director": "Christopher Nolan",
        "film_name": "Inception",
        "film_actor": "Leonardo DiCaprio"
    },
    {
        "id": 2,
        "film_certificate_id": 3,
        "film_blurb": """An astronaut becomes stranded on Mars after his team
                        assume him dead, and must rely on his ingenuity to find
                        a way to signal to Earth that he is alive.""",
        "film_director": "Ridley Scott",
        "film_name": "The Martian",
        "film_actor": "Matt Damon"
    },
    {
        "id": 3,
        "film_certificate_id": 3,
        "film_blurb": """A team of explorers travel through a wormhole in space
                            in an attempt to ensure humanity's survival""",
        "film_director": "Christopher Nolan",
        "film_name": "Interstellar",
        "film_actor": "Matthew McConaughey"
    },
    {
        "id": 4,
        "film_certificate_id": 2,
        "film_blurb": """Paddington, now happily settled with the Brown family
                        and a popular member of the local community, picks up a
                        series of odd jobs to buy the perfect present for his
                        Aunt Lucy's 100th birthday, """,
        "film_director": "Paul King",
        "film_name": "Paddington 2",
        "film_actor": "Ben Wishaw"
    },
    {
        "id": 5,
        "film_certificate_id": 4,
        "film_blurb": """A reclusive girl working in a high security American
                        government laboratory during the Cold War Era befriends
                        a strange, other-worldly creature who is part of a
                        secret classified experiment. """,
        "film_director": "Guillermo del Toro",
        "film_name": "The Shape of Water",
        "film_actor": "Sally Hawkins"
    },
    {
        "id": 6,
        "film_certificate_id": 3,
        "film_blurb": """T'Challa, the King of Wakanda, rises to the throne in
                        the isolated, technologically advanced African nation,
                        but his claim is challenged by a vengeful outsider who
                        was a childhood victim of T'Challa's father's mistake.""",
        "film_director": "Ryan Coogler",
        "film_name": "Black Panther",
        "film_actor": "Chadwick Boseman"
    },
    {
        "id": 7,
        "film_certificate_id": 2,
        "film_blurb": """P. T. Barnum is a man with little more than ambition to
                        his name. When the company he works for goes bust, he
                        decides to leave his mediocre life behind, and takes his
                        family on a journey that would lead to establishing the
                        foundations of showbusiness.""",
        "film_director": "Michael Gracey",
        "film_name": "The Greatest Showman",
        "film_actor": "Hugh Jackman"
    },
    {
        "id": 8,
        "film_certificate_id": 3,
        "film_blurb": """Four teenagers are sucked into a magical video game,
                        and the only way they can escape is to work together to
                        finish the game.""",
        "film_director": "Jake Kasden",
        "film_name": "Jumanji: Welcome to the Jungle",
        "film_actor": "Dwayne Johnson"
    },
    {
        "id": 9,
        "film_certificate_id": 1,
        "film_blurb": """Ignoring his family’s baffling ban on music, Miguel
                        embarks on a journey through the enchanting Land of the
                        Dead in search of his dreams of becoming a musician.""",
        "film_director": "Lee Unkrich",
        "film_name": "CoCo",
        "film_actor": "Anthony Gonzalez"
    }
]
print("populating movies (the FilmDetails table)")
for movie in filmData:
    newMovie = FilmDetails(**movie)
    db.session.add(newMovie)
    db.session.commit()

################################################################################

# Creates the TicketType table which remains unchanged and is used by the
# Ticket table.

ticketTypeData = [
    {
        "id": 1,
        "ticket_type": 1
    },
    {
        "id": 2,
        "ticket_type": 2
    },
    {
        "id": 3,
        "ticket_type": 3
    },
    {
        "id": 4,
        "ticket_type": 4
    },
    {
        "id": 5,
        "ticket_type": 5
    }
]

print("populating TicketType table")
for ticketType in ticketTypeData:
    newTicketType = TicketType(**ticketType)
    db.session.add(newTicketType)
    db.session.commit()

################################################################################

# Creates the Certificate table which remains unchanged and is used by the
# FilmDetails table.
# Certificates: 1=U , 2=PG, 3=12, 4=15, 5=18.

certificateData = [
    {
        "id": 1,
        "cert": 1
    },
    {
        "id": 2,
        "cert": 2
    },
    {
        "id": 3,
        "cert": 3
    },
    {
        "id": 4,
        "cert": 4
    },
    {
        "id": 5,
        "cert": 5
    }
]

print("populating certificates")
for certificate in certificateData:
    newCertificate = Certificate(**certificate)
    db.session.add(newCertificate)
    db.session.commit()

################################################################################

# Creates the Theatre table.

theatreData = [
    {
        "id": 1,
        "theatre_name": "Screen 1"
    },
    {
        "id": 2,
        "theatre_name": "Screen 2"
    },
    {
        "id": 3,
        "theatre_name": "Screen 3"
    }
]

print("populating theatre screens")
for screen in theatreData:
    newScreen = Theatre(**screen)
    db.session.add(newScreen)
    db.session.commit()

################################################################################

# Function to create random dates in the past month.


def random_date():
    year = datetime.now().year
    month = datetime.now().month - 1
    day = randint(1, monthrange(year, month)[1])
    randomDate = datetime(2018, month, day)

    return randomDate


# Populate the database with ticket data for 500 tickets.
print("generating random tickets")
for x in range(1, 501):
    sampleTicket = Ticket()
    sampleTicket.owner_account_id = randint(1, 100)
    sampleTicket.ticket_type_id = randint(1, 5)
    sampleTicket.ticket_screening_id = randint(1, 100)
    sampleTicket.ticket_date_bought = random_date()
    db.session.add(sampleTicket)
    db.session.commit()

# Populate the Seat table. This is constant - do not remove.
print("populating seats")
for x in range(1, 10):  # 9 theatres
    for y in range(1, 25):  # 24 seats in each theatre.
        newSeat = Seat()
        newSeat.seat_pos = y
        newSeat.theatre_id = x
        db.session.add(newSeat)
        db.session.commit()

# Function for creating consecutive dates to be used in the FilmScreening
# table.


def screening_date(x, z):

    if x < 32:
        month = 3
    elif (x > 31 and x < 62):
        month = 4
    elif (x > 61):
        month = 5

    if month == 3:
        screen_day = x

    elif month == 4:
        screen_day = (x % 31)

    elif month == 5:
        screen_day = ((x % 31) + 1)

    if z == 0:
        hours = 10
    elif z == 1:
        hours = 14
    elif z == 2:
        hours = 20

    screeningDate = datetime(2018, month, screen_day, hours, 0, 0)

    return screeningDate


# Populate the FilmScreening table.
print("populating film screenings")
for x in range(1, 68): # From 1st March to


    f = 1
    for z in range(0, 3):  # 3 different screening times per day
        for q in range(1, 4):  # 3 different cinema screens
            sampleScreening = FilmScreening()
            sampleScreening.film_screening_time = screening_date(x, z)
            sampleScreening.theatre_id = q
            sampleScreening.film_screening_film_det = f
            db.session.add(sampleScreening)
            db.session.commit()
            f = f + 1  # f is incremented to cycle through each film


# Create an admin Account.
print("Creating admin Account")
adminAccount = Account()
adminAccount.id = 1
adminAccount.email = 'movies.heron@gmail.com'
adminAccount.password = generate_password_hash('admin')
adminAccount.staff = True
db.session.add(adminAccount)
db.session.commit()

# Add cards belonging to the Admin account.
print("Creating Admin cards")
adminCard1 = Card()
adminCard1.id = 1
adminCard1.name_on_card = 'Admin'
adminCard1.billing_address = 'EC Stoner'
adminCard1.last_four_digits = 4444
adminCard1.card_number = 'hashedCardNumber'
adminCard1.cvc = 'hashedCVC'
adminCard1.expiry_date_month = 'hashedExpiryMonth'
adminCard1.expiry_date_year = 'hashedExpiryYear'
adminCard1.account_id = 1
db.session.add(adminCard1)
db.session.commit()

adminCard2 = Card()
adminCard2.id = 2
adminCard2.name_on_card = 'Admin'
adminCard2.billing_address = 'EC Stoner'
adminCard2.last_four_digits = 9999
adminCard2.card_number = 'hashedCardNumber2'
adminCard2.cvc = 'hashedCVC2'
adminCard2.expiry_date_month = 'hashedExpiryMonth2'
adminCard2.expiry_date_year = 'hashedExpiryYear2'
adminCard2.account_id = 1
db.session.add(adminCard2)
db.session.commit()
