from flask import render_template, request, url_for, redirect

from application import app

@app.route("/person", methods=["GET"])
def person_page():
    return render_template("person/page.html")

