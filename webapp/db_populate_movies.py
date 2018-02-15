from flask import Flask
from app.models import FilmDetails
from app import app, db, models
import json

sampleData = [
    {
      "age_certificate": 12, 
      "blurb": "Home alone, but on mars.", 
      "director": "Ridley Scott", 
      "film_name": "The Martian", 
      "id": 1, 
      "lead_actor": "Matt Damon"
    }, 
    {
      "age_certificate": 1, 
      "blurb": "Professor has unusually productive sabatical.", 
      "director": "Steven Spielberg", 
      "film_name": "Raiders of the Lost Ark", 
      "id": 2, 
      "lead_actor": "Harrison Ford"
    }, 
    {
      "age_certificate": 15, 
      "blurb": "Professor finds a shiny head.", 
      "director": "Steven Spielberg", 
      "film_name": "Indiana Jones and the Kingdom of the Crystal Skull", 
      "id": 3, 
      "lead_actor": "Harrison Ford"
    }
    ]

for movie in sampleData:
    newMovie = FilmDetails(**movie)
    db.session.add(newMovie)
    db.session.commit()
