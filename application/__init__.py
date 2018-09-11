#Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)


#Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

#Käytetään tasks.db-nimistä SQLite -tietokantaa.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
#Pyydetään SQLAlchemyä tuomaan kaikki SQL -kyselyt
app.config["SQLALCHEMY_ECHO"] = True
#Luodaan db-olio jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

#Luetaan kansiosta application tietoston views sisältö
from application import views

#Tuodaan models luokka application käyttöön
from application.tasks import models

#Luodaan lopulta tarvittavat tietokantataulut
db.create_all()