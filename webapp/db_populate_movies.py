from flask import Flask
from app.models import FilmDetails
from app import app, db, models
import json

sampleData = [
    {
        << << << < 0cda86d41cca84e4915db9f9e885404d674d4dac
        "filmCertificate": 12,
        "filmBlurb": "Home alone, but on mars.",
        "filmDirector": "Ridley Scott",
        "filmName": "The Martian",
        "filmActor": "Matt Damon"
    },
    {
        "filmCertificate": 1,
        "filmBlurb": "Professor has unusually productive sabatical.",
        "filmDirector": "Steven Spielberg",
        "filmName": "Raiders of the Lost Ark",
        "filmActor": "Harrison Ford"
    },
    {
        "filmCertificate": 15,
        "filmBlurb": "Professor finds a shiny head.",
        "filmDirector": "Steven Spielberg",
        "filmName": "Indiana Jones and the Kingdom of the Crystal Skull",
        "filmActor": "Harrison Ford"
    }
]
== == == =
>>>>>> > bringing other files uptodate to continue test development

for movie in sampleData:
    newMovie = FilmDetails(**movie)
    db.session.add(newMovie)
    db.session.commit()
