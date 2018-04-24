from flask import Flask, request, jsonify
from .models import FilmDetails, Ticket, FilmScreening
from app import app, db, models
import json


@app.route('/api/films', methods=['GET'])
def apiGetMovies():
    """Returns all films in then database in JSON format

    Returns: A JSON object containing details of all films in the database
    """
    films = FilmDetails.query.all()
    return jsonify({"films": films})


@app.route('/api/tickets', methods=['GET'])
def apiGetTickets():
    """Returns all tickets in the database in JSON format
    """
    tickets = Ticket.query.all()
    return jsonify({"tickets": tickets})


@app.route('/api/tickets/screening/<int:id>', methods=['GET'])
def apiGetScreeningTickets(id):
    tickets = Ticket.query.filter_by(ticket_screening_id=id).all()
    return jsonify({"tickets": tickets})


@app.route('/api/films/<int:id>/screenings', methods=['GET'])
def apiGetMovieScreenings(id):
    screenings = FilmScreening.query.filter_by(film_screening_film_det=id).all()
    return jsonify({"screenings": screenings})
