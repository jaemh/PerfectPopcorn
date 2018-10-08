from application import db

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)


def __repr__(self):
    return '<Movie %r>' % self.name 