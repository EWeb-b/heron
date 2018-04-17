from flask import Flask
from app.models import FilmDetails
from app import app, db, models
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
        "ticketDateBought": 2018 - 14 - 01 15: 01: 10,

    },
    {
        "id": 2,
        "ownerProfileId": 1,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": 2018 - 14 - 01 15: 01: 10,

    },
    {
        "id": 3,
        "ownerProfileId": 1,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": 2018 - 14 - 01 15: 01: 10,

    },
    {
        "id": 4,
        "ownerProfileId": 2,
        "ticketTypeId": 2,
        "ticketScreeningId": 1,
        "ticketDateBought": 2018 - 14 - 01 16: 01: 10,

    },
    {
        "id": 5,
        "ownerProfileId": 2,
        "ticketTypeId": 2,
        "ticketScreeningId": 1,
        "ticketDateBought": 2018 - 14 - 01 16: 01: 10,

    },
    {
        "id": 6,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": 2018 - 14 - 01 17: 01: 10,

    },
    {
        "id": 7,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": 2018 - 14 - 01 17: 01: 10,

    },
    {
        "id": 8,
        "ownerProfileId": 3,
        "ticketTypeId": 1,
        "ticketScreeningId": 1,
        "ticketDateBought": 2018 - 14 - 01 17: 01: 10,

    }
]

for aTicket in ticketData:
    newTicket = Ticket(**aTicket)
    db.session.add(newTicket)
    db.session.commit()
