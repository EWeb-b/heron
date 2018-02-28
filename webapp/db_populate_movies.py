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

for movie in sampleData:
    newMovie = FilmDetails(**movie)
    db.session.add(newMovie)
    db.session.commit()
