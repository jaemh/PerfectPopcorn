from application import db

class Movie(db.Model):
    __tablename__ = 'movie'
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(20), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'), nullable=False)
    genre = db.relationship('Genre', backref='genre')   

    def __init__(self, name, genre):
        self.movie_name=name
        self.genre = genre
    
class Genre(db.Model):
    __tablename__ = 'genre'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String)

    def __init__(self, name):
        self.genre_name=name

