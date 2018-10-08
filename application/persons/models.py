from application import db


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    movies = db.relationship("Movie", 
                secondary=movies,
                backref=db.backref("persons", lazy="dynamic"),
                )
        
    def __repr__(self):
        return '<Person %r>' % self.name

    
movies = db.Table('movies',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    ) 