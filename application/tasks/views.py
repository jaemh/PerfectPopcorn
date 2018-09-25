from flask import render_template, request, url_for, redirect

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/", methods=["GET"])
def tasks_index():
    return render_template("index.html")

@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())

@app.route("/tasks/<task_id>/", methods=["POST"])
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    t.done = True
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
def tasks_create():
    t = Task(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))