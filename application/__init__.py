#Tuodaan Flask käyttöön
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


#Luetaan kansiosta application tietoston views sisältö
from application import views

#Tuodaan luokat application käyttöön
from application.tasks import models
from application.tasks import views

from application.auth import models
from application.auth import views

from application.movies import models
from application.movies import views


#kirjautuminen

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_massage = "Please login to use this funcionality."
from application.movies.models import Genre

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def insert_genres():
    print("genret: ")
    genres = Genre.query.all()
    print(genres)

    if len(genres) == 0:
      print("genret empty ")
      action = Genre('Action')
      comedy = Genre('Comedy')
      drama = Genre('Drama')
      fantasy = Genre('Fantasy')
      historical = Genre('Historical')
      db.session.add(action)
      db.session.add(comedy)
      db.session.add(drama)
      db.session.add(fantasy)
      db.session.add(historical)
      db.session.commit()
    

#Luodaan lopulta tarvittavat tietokantataulut
try: 
    db.create_all()
except:
    pass

try: 
    insert_genres()
except:
    pass