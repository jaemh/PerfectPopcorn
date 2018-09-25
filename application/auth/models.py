from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
   
  
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