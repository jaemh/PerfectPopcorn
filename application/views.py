from flask import render_template
from application import app
from application.movies.models import Movie

@app.route("/")
def intex():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies )
    
    