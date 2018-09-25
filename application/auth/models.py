from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    