from flask import Flask, request, jsonify
from .models import FilmDetails, Ticket, FilmScreening
from app import app, db, models
from datetime import datetime, date
from isoweek import Week


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


@app.route('/api/films/<int:film>/screenings', methods=['GET'])
def apiGetMovieScreenings(film):
    """Returns all screenings for the given film
    """
    screenings = FilmScreening.query.filter_by(film_screening_film_det=film).all()
    return jsonify({"screenings": screenings})


@app.route('/api/tickets/screening/<int:screening>', methods=['GET'])
def apiGetTicketsForScreening(screening):
    """Returns all tickets for the given screening
    """
    tickets = Ticket.query.filter_by(ticket_screening_id=screening).all()
    return jsonify({"tickets": tickets})


@app.route('/api/screenings', methods=['GET'])
def apiGetScreenings():
    """Returns all screenings in the database
    """
    screenings = FilmScreening.query.all()
    return jsonify({"screenings": screenings})


@app.route('/api/tickets/weekly/<int:year>/<int:week>', methods=['GET'])
def apiGetWeeklyTickets(year, week):
    """ Returns all tickets for the given week
    """
    start_day = Week(year, week).monday()
    end_day = Week(year, week).sunday()


    tickets = Ticket.query.join(FilmScreening).
    return jsonify({"tickets": tickets})
