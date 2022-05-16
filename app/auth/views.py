from flask import render_template,redirect,url_for,flash
from . import auth
from ..models import User
from .forms import RegistrationForm
from .. import db

# Registration view function
@auth.route('/register',methods = ['GET', 'POST'])
def register():
    '''
    register function to register new users and add them into the database.
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        flash(f'New account setup for {form.username.data}')

        return redirect(url_for('auth.login'))
        title = 'New Account'
    return render_template('auth/register.html', registration_form = form)


@auth.route('/login')
def login():
    

    return render_template('auth/login.html')
