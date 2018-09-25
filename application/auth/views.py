from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return render_template("index.html") 

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/signup.html", form = RegistrationForm())
    
    form = RegistrationForm(request.form)
    
    if request.method == 'POST':
       new_user = User(name=form.name.data, username=form.username.data, password=form.password.data)
       db.session.add(new_user)
       db.session.commit()
       return "New user has been created!"

@app.route("/logout")
def logout():
    logout_user()
    return render_template("index.html")