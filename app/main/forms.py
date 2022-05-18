from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField, SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    '''
    UpdateProfile class to create instances of updateprofile objects
    '''
    bio = TextAreaField('Tell us a little about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class PostBlog(FlaskForm):
    '''
    PostBlog class to create instances of blog objects
    '''
    content = TextAreaField('Write your blog post', validators= [InputRequired()])
    author = TextAreaField('Name of author', validators = [InputRequired()])
    category = SelectField('Category', choices=(['', 'Food', 'Sports', 'Travel', 'Art', 'Music', 'Film', 'Lifestyle', 'Automobiles', 'Other']), validators = [InputRequired()])
    submit = SubmitField('Post')

class PostComment(FlaskForm):
    '''
    PostComment class to create instances of comment obj
    '''
    content = TextAreaField('Write a comment', validators = [InputRequired()])
    submit = SubmitField('Post')