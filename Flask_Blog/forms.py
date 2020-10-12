"""
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Python class inheriting flaskfrom which generates the corresponding html
class RegistrationForm(FlaskForm):
    
    # With input data validation
    username = StringField('Username', 
                           validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sigh Up')
    

# Python class inheriting flaskfrom which generates the corresponding html
class LoginForm(FlaskForm):
    
    # With input data validation
    email = StringField('Email', 
                        validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')