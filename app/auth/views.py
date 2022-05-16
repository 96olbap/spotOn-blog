from turtle import title
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
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
    return render_template('auth/register.html', registration_form = form, title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    login view function to login a registered user
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)

            flash(f'Hello, welcome back')

            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "User login"

    return render_template('auth/login.html',login_form = login_form,title=title)