from flask import render_template

from application.movies.models import Movie
from application import app

@app.route("/action", methods=["GET"])
def all_action_movies():
    movies = Movie.query.all()
    return render_template("movies/action.html", movies=movies)
