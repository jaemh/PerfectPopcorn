from application import db

class Movie(db.Model):
    __tablename__ = 'movie'
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(20), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'), nullable=False)
    genre = db.relationship('Genre', backref='genre')
    posts = db.relationship('Post', backref='film', lazy=True)

    def __init__(self, name, genre):
        self.movie_name=name
        self.genre=genre
        
        
    
class Genre(db.Model):
    __tablename__ = 'genre'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String)

    def __init__(self, name, id):
        self.genre_name=name,
        self.genre_id=id

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_text = db.Column(db.String(500), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'),
        nullable=False)

    def __init__(self, text, movie_id):
        self.post_text=text
        self.movie_id=movie_id

