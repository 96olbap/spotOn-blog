from flask import render_template,redirect,request,url_for,abort
from ..models import User,Blog_post
from . import main
from .forms import UpdateProfile,PostBlog
from .. import db,photos
from flask_login import login_required,current_user

# Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    form = PostBlog()

    blogs = Blog_post.query.all()

    if form.validate_on_submit():
        blog = Blog_post(content = form.content.data, author = form.author.data, category = form.category.data, user_id = current_user.id)
        db.session.add(blog)
        db.session.commit()


    return render_template('index.html', form=form, blogs=blogs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))