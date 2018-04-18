from flask import Flask
from app.models import FilmDetails, Ticket
from app import app, db, models
from datetime import datetime
import json

filmData = [
    {
        "id": 1,
        "filmCertificateId": 12,
        "filmBlurb": "Entering dreams.",
        "filmDirector": "Christopher Nolan",
        "filmName": "Inception",
        "filmActor": "Leonardo DiCaprio"
    },
    {
        "id": 2,
        "filmCertificateId": 12,
        "filmBlurb": "Home alone, but on mars.",
        "filmDirector": "Ridley Scott",
        "filmName": "The Martian",
        "filmActor": "Matt Damon"
    },
    {
        "id": 3,
        "filmCertificateId": 12,
        "filmBlurb": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival",
        "filmDirector": "Christopher Nolan",
        "filmName": "Interstellar",
        "filmActor": "Matthew McConaughey"
    },
    {
        "id": 4,
        "filmCertificateId": 12,
        "filmBlurb": "Peruvain Bear up to no good",
        "filmDirector": "Paul King",
        "filmName": "Paddington 2",
        "filmActor": "Ben Wishaw"
    },
    {
        "id": 5,
        "filmCertificateId": 15,
        "filmBlurb": "Fishman seduces silent woman",
        "filmDirector": "Guillermo del Toro",
        "filmName": "The Shape of Water",
        "filmActor": "Sally Hawkins"
    },
    {
        "id": 6,
        "filmCertificateId": 12,
        "filmBlurb": "",
        "filmDirector": "Ryan Coogler",
        "filmName": "Black Panther",
        "filmActor": "Chadwick Boseman"
    },
    {
        "id": 7,
        "filmCertificateId": 12,
        "filmBlurb": "Hugh Jackman's career takes a suspect turn",
        "filmDirector": "Michael Gracey",
        "filmName": "The Greatest  Showman",
        "filmActor": "Hugh Jackman"
    },
    {
        "id": 8,
        "filmCertificateId": 12,
        "filmBlurb": "Horrible remake",
        "filmDirector": "Jake Kasden",
        "filmName": "Jumanji: Welcome to the jungle",
        "filmActor": "Dwayne Johnson"
    },
    {
        "id": 9,
        "filmCertificateId": 12,
        "filmBlurb": "Undead reconcilliation",
        "filmDirector": "Lee Unkrich",
        "filmName": "CoCo",
        "filmActor": "Anthony Gonzalez"
    }
]

for movie in filmData:
    newMovie = FilmDetails(**movie)
    db.session.add(newMovie)
    db.session.commit()

ticketData = [

    {
        "id": 1,
        "ownerProfileId": 1,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

    },
    {
        "id": 2,
        "ownerProfileId": 1,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

    },
    {
        "id": 3,
        "ownerProfileId": 1,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

    },
    {
        "id": 4,
        "ownerProfileId": 2,
        "ticketTypeId": 2,
        "ticketScreeningId": 1,
        "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

    },
    {
        "id": 5,
        "ownerProfileId": 2,
        "ticketTypeId": 2,
        "ticketScreeningId": 1,
        "ticketDateBought": datetime(2018, 4, 1, 15, 1, 10)

    },
    {
        "id": 6,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": datetime(2018, 4, 1, 17, 1, 10)

    },
    {
        "id": 7,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": datetime(2018, 4, 1, 17, 1, 10)

    },
    {
        "id": 8,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": datetime(2018, 4, 1, 17, 1, 10)

    },
    {
        "id": 9,
        "ownerProfileId": 1,
        "ticketTypeId": 1,
        "ticketScreeningId": 11,
        "ticketDateBought": datetime(2018, 4, 12, 15, 1, 10)

    },
    {
        "id": 10,
        "ownerProfileId": 1,
        "ticketTypeId": 1,
        "ticketScreeningId": 11,
        "ticketDateBought": datetime(2018, 4, 12, 15, 1, 10)

    },
    {
        "id": 11,
        "ownerProfileId": 1,
        "ticketTypeId": 1,
        "ticketScreeningId": 11,
        "ticketDateBought": datetime(2018, 4, 12, 15, 1, 10)

    },
    {
        "id": 12,
        "ownerProfileId": 2,
        "ticketTypeId": 2,
        "ticketScreeningId": 11,
        "ticketDateBought": datetime(2018, 4, 12, 16, 1, 10)

    },
    {
        "id": 13,
        "ownerProfileId": 2,
        "ticketTypeId": 2,
        "ticketScreeningId": 11,
        "ticketDateBought": datetime(2018, 4, 12, 16, 1, 10)

    },
    {
        "id": 14,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 11,
        "ticketDateBought": datetime(2018, 4, 12, 17, 1, 10)

    },
    {
        "id": 15,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 11,
        "ticketDateBought": datetime(2018, 4, 12, 17, 1, 10)

    },
    {
        "id": 16,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 11,
        "ticketDateBought": datetime(2018, 4, 12, 17, 1, 10)

    }
]

for aTicket in ticketData:
    newTicket = Ticket(**aTicket)
    db.session.add(newTicket)
    db.session.commit()
