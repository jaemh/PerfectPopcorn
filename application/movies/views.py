from flask import render_template, request, url_for, redirect
from application.auth.forms import RegistrationForm
from application import app, db
from application.auth.models import User
from application.movies.forms import MovieForm
from application.movies.models import Movie, Genre, Post
from flask_login import current_user, login_required


@app.route("/person", methods=["GET"])
def person_page():
    user = User.query.get(current_user.id)
    post = Post.query.all()
    return render_template("movies/page.html", user=user, post=post)

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

@app.route("/movies/<movie_id>/comments/")
def b(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template("movies/movie_page.html", movie=movie)

@app.route("/movies/<movie_id>/comments/", methods=["POST"])
def create_post(movie_id):
    comment = request.form.get('comment')
    post = Post(comment, movie_id)

    db.session().add(post)
    db.session().commit()

    return b(movie_id) 

@app.route("/genre/<genre_id>")
def genre_page(genre_id):
    genres = Genre.query.filter_by(genre_id="1").first()
    return render_template("movies/genre_page.html", genres=genres)






