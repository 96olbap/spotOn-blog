from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()], render_kw={"placeholder": "example@example.com"})
    username = StringField('Enter your username',validators = [InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('Password',validators = [InputRequired(), EqualTo('password_confirm',message = 'Passwords must match')], render_kw={"placeholder": "Set a password"})
    password_confirm = PasswordField('Confirm Passwords',validators = [InputRequired()], render_kw={"placeholder":"Confirm Password"})
    submit = SubmitField('Sign Up')

    # Custom validators
    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is already an account with that email, please choose another one')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()], render_kw={"placeholder": "example@example.com"})
    password = PasswordField('Password',validators =[InputRequired()], render_kw={"placeholder":"********"})
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')