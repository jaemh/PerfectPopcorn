from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class MovieForm(FlaskForm):
    name = StringField("Movie name")
  
class Meta:
    csrf = False

class PostForm(FlaskForm):
    comment = StringField("Comment")