from flask import render_template

from application.movies.models import Movie
from application import app

@app.route("/action", methods=["GET"])
def all_action_movies():
    movies = Movie.query.all()
    return render_template("movies/action.html", movies=movies)

@app.route("/comedy", methods=["GET"])
def all_comedy_movies():
    movies = Movie.query.all()
    return render_template("movies/comedy.html", movies=movies)

@app.route("/fantacy", methods=["GET"])
def all_fantacy_movies():
    movies = Movie.query.all()
    return render_template("movies/fantacy.html", movies=movies)

@app.route("/drama", methods=["GET"])
def all_drama_movies():
    movies = Movie.query.all()
    return render_template("movies/drama.html", movies=movies)

@app.route("/historical", methods=["GET"])
def all_historical_movies():
    movies = Movie.query.all()
    return render_template("movies/historical.html", movies=movies)