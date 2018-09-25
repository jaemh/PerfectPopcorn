from flask_wtf import FlaskForm 
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, Length

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=4, max=10)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=10)])
    password = PasswordField('New Password', validators=[InputRequired(), Length(min=4, max=10)])
   

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
  
    class Meta:
        csrf = False