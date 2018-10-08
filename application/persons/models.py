from application import db

movies = db.Table('movies',
        db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id')),
        db.Column('id', db.Integer, db.ForeignKey('person.id'))
)


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    mov = db.relationship('Movie', 
                secondary=movies,
                backref=db.backref('movie', lazy='dynamic'),
)
        
    def __init__(self, name):
        self.id = id
		