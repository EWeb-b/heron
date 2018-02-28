from flask import Flask
from app.models import FilmDetails
from app import app, db, models
import json

sampleData = [
    {
        "filmCertificate": 12,
        "filmBlurb": "Entering dreams.",
        "filmDirector": "Christopher Nolan",
        "filmName": "Inception",
        "filmActor": "Leonardo DiCaprio"
    },
    {
        "filmCertificate": 12,
        "filmBlurb": "Home alone, but on mars.",
        "filmDirector": "Ridley Scott",
        "filmName": "The Martian",
        "filmActor": "Matt Damon"
    },
    {
        "filmCertificate": 12,
        "filmBlurb": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival",
        "filmDirector": "Christopher Nolan",
        "filmName": "Interstellar",
        "filmActor": "Matthew McConaughey"
    },
    {
        "filmCertificate": 18,
        "filmBlurb": "Post apocolyptic madness",
        "filmDirector": "George Miller",
        "filmName": "Mad Max: Fury Road",
        "filmActor": "Tom Hardy"
    }
]

for movie in sampleData:
    newMovie = FilmDetails(**movie)
    db.session.add(newMovie)
    db.session.commit()
