from flask import Flask
from app.models import (FilmDetails, Ticket, Seat, Theatre, Certificate,
                        TicketType)
from app import app, db, models
from datetime import datetime
import json
import random



################################################################################

# Populates the FilmDetails table with films.
# Certificates 1=U , 2=PG, 3=12, 4=15, 5=18.

filmData = [
    {
        "id": 1,
        "film_certificate_id": 3,
        "film_blurb": "Entering dreams.",
        "film_director": "Christopher Nolan",
        "film_name": "Inception",
        "film_actor": "Leonardo DiCaprio"
    },
    {
        "id": 2,
        "film_certificate_id": 3,
        "film_blurb": "Home alone, but on mars.",
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
        "film_blurb": "Peruvain Bear up to no good",
        "film_director": "Paul King",
        "film_name": "Paddington 2",
        "film_actor": "Ben Wishaw"
    },
    {
        "id": 5,
        "film_certificate_id": 4,
        "film_blurb": "Fishman seduces silent woman",
        "film_director": "Guillermo del Toro",
        "film_name": "The Shape of Water",
        "film_actor": "Sally Hawkins"
    },
    {
        "id": 6,
        "film_certificate_id": 3,
        "film_blurb": "superhero movie",
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
        "film_name": "The Greatest  Showman",
        "film_actor": "Hugh Jackman"
    },
    {
        "id": 8,
        "film_certificate_id": 3,
        "film_blurb": "Horrible remake",
        "film_director": "Jake Kasden",
        "film_name": "Jumanji: Welcome to the jungle",
        "film_actor": "Dwayne Johnson"
    },
    {
        "id": 9,
        "film_certificate_id": 1,
        "film_blurb": "Undead reconcilliation",
        "film_director": "Lee Unkrich",
        "film_name": "CoCo",
        "film_actor": "Anthony Gonzalez"
    }
]

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
    },
    {
        "id": 4,
        "theatre_name": "Screen 4"
    },
    {
        "id": 5,
        "theatre_name": "Screen 5"
    },
    {
        "id": 6,
        "theatre_name": "Screen 6"
    },
    {
        "id": 7,
        "theatre_name": "Screen 7"
    },
    {
        "id": 8,
        "theatre_name": "Screen 8"
    },
    {
        "id": 9,
        "theatre_name": "Screen 9"
    }
]

for screen in theatreData:
    newScreen = Theatre(**screen)
    db.session.add(newScreen)
    db.session.commit()

################################################################################

# Function to create random dates in the past month.
def random_date():
    month = random.randint(3, 4)
    day = random.randint(1, 20)
    randomDate = datetime(2018, month, day)

    return randomDate

# Populate the database with ticket data for 500 tickets.
# for x in range(1, 501):
#     sampleTicket = Ticket()
#     sampleTicket.owner_profile_id = random.randint(1, 100)
#     sampleTicket.ticket_type_id = random.randint(1, 5)
#     sampleTicket.ticket_screening_id = random.randint(1, 9)
#     sampleTicket.ticket_date_bought = random_date()
#     db.session.add(sampleTicket)
#     db.session.commit()

# Populate the Seat table. This is constant - do not remove.
for x in range(1,10):
    for y in range(1,25): # 24 seats in each theatre.
        newSeat = Seat()
        newSeat.seat_pos = y
        newSeat.theatre_id = x
        db.session.add(newSeat)
        db.session.commit()
