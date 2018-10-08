from flask import render_template, request, url_for, redirect
from application.auth.forms import RegistrationForm
from application import app

@app.route("/person", methods=["GET"])
def person_page():
    return render_template("person/page.html")

@app.route("/edit")
def person_edit():
    form = RegistrationForm(request.form)

    return render_template("auth/signup.html", form = RegistrationForm())