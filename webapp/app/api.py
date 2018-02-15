from flask import Flask, request, jsonify
from .models import FilmDetails
from app import app, db, models
import json


@app.route('/api/movies', methods=['GET'])
def apiGetMovies():
    """Returns all films in then database in JSON format

    Returns: A JSON object containing details of all films in the database
    """
    movies = FilmDetails.query.all()
    return jsonify({"films": FilmDetails.serializeList(movies)})


@app.route('/api/movies', methods=['POST'])
def apiNewMovie():
    """Adds a new film to the database via a POST request containing JSON data
    for the new movie"""
    if not request.json or 'film_name' not in request.json:
        abort(404)
    movie = FilmDetails(**request.json)
    db.session.add(movie)
    db.session.commit()
    return 'test', 201
