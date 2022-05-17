from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    '''
    load_user function to retrieve a user when a unique identifier is passed
    '''
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    '''
    User class that will define user objects
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80), index = True)
    email = db.Column(db.String(255),unique= True, index = True)
    bio =db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    post = db.relationship('Blog_post', backref = 'posts', lazy = 'dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User { self.username }'

class Blog_post(db.Model):
    '''
    Blog_post class that will define post objects
    '''
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255), nullable = False)
    author = db.Column(db.String(80), nullable = False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category = db.Column(db.String(), nullable = False)
    like = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref = 'comments', lazy = 'dynamic')

    def __repr__(self):
        return f'Blog_post { self.content }'

class Comment(db.Model):
    '''
    Comments class to define coment objects
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255), nullable = False)
    posted_at = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    blog_post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

        @classmethod
        def get_comments(cls,id):
            comments = Comment.query.filter_by(blog_post_id=id).all()
            return comments

    def __repr__(self):
        return f'User {self.content}'
