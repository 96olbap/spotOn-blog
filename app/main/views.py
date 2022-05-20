from unicodedata import category
from flask import render_template,redirect,request,url_for,abort
from sqlalchemy import desc
from ..models import User,Blog_post,Comment
from . import main
from .forms import UpdateProfile,PostBlog,PostComment
from .. import photos,db
from flask_login import login_required,current_user
from ..requests import process_quote

# Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    form = PostBlog()
    quote = process_quote()
    title = 'Home - SpotOnBlog'

    blogs = Blog_post.query.order_by(desc(Blog_post.created_at))

    if request.method == 'POST':

        if form.validate_on_submit():
            post = Blog_post(content = form.content.data, author = form.author.data, category = form.category.data, user_id = current_user.id)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('.index')) 


    return render_template('index.html', form=form, blogs=blogs, quote=quote, title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    posts = Blog_post.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user, posts = posts)

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

@main.route('/comment/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def make_comment(blog_id):

    blog = Blog_post.query.filter_by(id = blog_id).first()
    comments = Comment.query.filter_by(blog_post_id = blog_id)

    if blog is None:
        abort(404)


    form = PostComment()

    if form.validate_on_submit():
        added_comment = Comment(content = form.content.data, blog_post_id = blog_id, user_id = current_user.id)

        db.session.add(added_comment)
        db.session.commit()

        return redirect(url_for('.make_comment', blog_id = blog_id))
    title = 'SpotOnBlog | Comments'

    return render_template('comment/comment.html', form = form, blog = blog, comments = comments, title = title)
