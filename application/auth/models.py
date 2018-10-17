from application import db

movies = db.Table('movies',
        db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id')),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    posts = db.relationship('Post', backref="comment", lazy=True)
    seenMovies = db.relationship('Movie', 
                secondary=movies,
                backref=db.backref('movie', lazy='dynamic')
    )
   
  
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        
    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True