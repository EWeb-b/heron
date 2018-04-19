from flask import Flask
from app.models import FilmDetails, Ticket
from app import app, db, models
from datetime import datetime
import json
import random
filmData = [
    {
        "id": 1,
        "film_certificate_id": 12,
        "film_blurb": "Entering dreams.",
        "film_director": "Christopher Nolan",
        "film_name": "Inception",
        "film_actor": "Leonardo DiCaprio"
    },
    {
        "id": 2,
        "film_certificate_id": 12,
        "film_blurb": "Home alone, but on mars.",
        "film_director": "Ridley Scott",
        "film_name": "The Martian",
        "film_actor": "Matt Damon"
    },
    {
        "id": 3,
        "film_certificate_id": 12,
        "film_blurb": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival",
        "film_director": "Christopher Nolan",
        "film_name": "Interstellar",
        "film_actor": "Matthew McConaughey"
    },
    {
        "id": 4,
        "film_certificate_id": 12,
        "film_blurb": "Peruvain Bear up to no good",
        "film_director": "Paul King",
        "film_name": "Paddington 2",
        "film_actor": "Ben Wishaw"
    },
    {
        "id": 5,
        "film_certificate_id": 15,
        "film_blurb": "Fishman seduces silent woman",
        "film_director": "Guillermo del Toro",
        "film_name": "The Shape of Water",
        "film_actor": "Sally Hawkins"
    },
    {
        "id": 6,
        "film_certificate_id": 12,
        "film_blurb": "superhero movie",
        "film_director": "Ryan Coogler",
        "film_name": "Black Panther",
        "film_actor": "Chadwick Boseman"
    },
    {
        "id": 7,
        "film_certificate_id": 12,
        "film_blurb": "Hugh Jackman's career takes a suspect turn",
        "film_director": "Michael Gracey",
        "film_name": "The Greatest  Showman",
        "film_actor": "Hugh Jackman"
    },
    {
        "id": 8,
        "film_certificate_id": 12,
        "film_blurb": "Horrible remake",
        "film_director": "Jake Kasden",
        "film_name": "Jumanji: Welcome to the jungle",
        "film_actor": "Dwayne Johnson"
    },
    {
        "id": 9,
        "film_certificate_id": 12,
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

# ticketData = [

#     {
#         "id": 1,
#         "ownerProfileId": 1,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 1,
#         "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

#     },
#     {
#         "id": 2,
#         "ownerProfileId": 1,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 1,
#         "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

#     },
#     {
#         "id": 3,
#         "ownerProfileId": 1,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 1,
#         "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

#     },
#     {
#         "id": 4,
#         "ownerProfileId": 2,
#         "ticketTypeId": 2,
#         "ticketScreeningId": 1,
#         "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

#     },
#     {
#         "id": 5,
#         "ownerProfileId": 2,
#         "ticketTypeId": 2,
#         "ticketScreeningId": 1,
#         "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

#     },
#     {
#         "id": 6,
#         "ownerProfileId": 3,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 1,
#         "ticketDateBought": datetime(2018, 4, 1, 17, 1, 10)

#     },
#     {
#         "id": 7,
#         "ownerProfileId": 3,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 1,
#         "ticketDateBought": datetime(2018, 4, 1, 17, 1, 10)

#     },
#     {
#         "id": 8,
#         "ownerProfileId": 3,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 1,
#         "ticketDateBought": datetime(2018, 4, 1, 17, 1, 10)

#     },
#     {
#         "id": 9,
#         "ownerProfileId": 1,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 11,
#         "ticketDateBought": datetime(2018, 4, 12, 15, 1, 10)

#     },
#     {
#         "id": 10,
#         "ownerProfileId": 1,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 11,
#         "ticketDateBought": datetime(2018, 4, 12, 15, 1, 10)

#     },
#     {
#         "id": 11,
#         "ownerProfileId": 1,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 11,
#         "ticketDateBought": datetime(2018, 4, 12, 15, 1, 10)

#     },
#     {
#         "id": 12,
#         "ownerProfileId": 2,
#         "ticketTypeId": 2,
#         "ticketScreeningId": 11,
#         "ticketDateBought": datetime(2018, 4, 12, 16, 1, 10)

#     },
#     {
#         "id": 13,
#         "ownerProfileId": 2,
#         "ticketTypeId": 2,
#         "ticketScreeningId": 11,
#         "ticketDateBought": datetime(2018, 4, 12, 16, 1, 10)

#     },
#     {
#         "id": 14,
#         "ownerProfileId": 3,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 11,
#         "ticketDateBought": datetime(2018, 4, 12, 17, 1, 10)

#     },
#     {
#         "id": 15,
#         "ownerProfileId": 3,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 11,
#         "ticketDateBought": datetime(2018, 4, 12, 17, 1, 10)

#     },
#     {
#         "id": 16,
#         "ownerProfileId": 3,
#         "ticketTypeId": 1,
#         "ticketScreeningId": 11,
#         "ticketDateBought": datetime(2018, 4, 12, 17, 1, 10)

#     }
# ]

# for aTicket in ticketData:
#     newTicket = Ticket(**aTicket)
#     db.session.add(newTicket)
#     db.session.commit()


# Function to create random dates in the past month
def random_date():
    month = random.randint(3, 4)
    day = random.randint(1, 20)
    randomDate = datetime(2018, month, day)

    return randomDate

# Populate the database with ticket data.
for x in xrange(1, 1000):
    sampleTicket = Ticket()
    sampleTicket.owner_profile_id = random.randint(1, 100)
    sampleTicket.ticket_type_id = random.randint(1, 5)
    sampleTicket.ticket_screening_id = random.randint(1, 9)
    sampleTicket.ticket_date_bought = random_date()
    db.session.add(sampleTicket)
    db.session.commit()
