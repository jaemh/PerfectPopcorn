from flask import render_template, request, url_for, redirect
from application.auth.forms import RegistrationForm
from application import app, db
from application.persons.forms import MovieForm
from application.movies.models import Movie


@app.route("/person", methods=["GET"])
def person_page():
    return render_template("person/page.html")

@app.route("/edit")
def person_edit():
    form = RegistrationForm(request.form)

    return render_template("auth/signup.html", form = RegistrationForm())

@app.route("/person/new/")
def movie_form():
    return render_template("person/new_movie.html", form = MovieForm())

@app.route("/person/", methods=["POST"])
def create_movie():
    f = Movie(request.form.get('name'))
  
    db.session().add(f)
    db.session().commit()
  
    return redirect(url_for("person_page"))