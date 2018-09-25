from flask import render_template, request, url_for, redirect

from application import app

@app.route("/movies", methods=["GET"])
def action_movie():
    return render_template("movies/action.html")

