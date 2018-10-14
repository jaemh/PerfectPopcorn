from flask import render_template, request, url_for, redirect
from application.auth.forms import RegistrationForm
from application import app, db
from application.auth.models import User
from application.movies.forms import MovieForm
from application.movies.models import Movie, Genre
from flask_login import current_user, login_required


@app.route("/person", methods=["GET"])
def person_page():
    user = User.query.get(current_user.id)
    return render_template("movies/page.html", user=user)

@app.route("/edit")
def person_edit():
    form = RegistrationForm(request.form)
    return render_template("auth/signup.html", form = RegistrationForm())

@app.route("/person/new/")
def movie_form():
    return render_template("movies/new_movie.html", form = MovieForm())

@app.route("/person/", methods=["POST"])
@login_required
def create_movie():
    f = Movie.query.filter_by(movie_name=request.form.get('name')).first()

    if f is None: 
        f = Movie(request.form.get('name'), Genre.query.get(request.form.get('genre')))

    userId = current_user.id
    user = User.query.get(userId)
    user.seenMovies.append(f) #tekee liittämisen
    db.session().add(user)
    db.session().commit()

    return person_page()

@app.route("/movie/")
def movie_page():
    return render_template("movies/movie_page.html")

@app.route("/genre/<genre_id>")
def genre_page(genre_id):
    genres = Genre.query.filter_by(genre_id="1").first()
    return render_template("movies/genre_page.html", genres=genres)


