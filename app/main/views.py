from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm
from ..models import Review, User
# Review = review.Review
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Blogs'
    return render_template('index.html',message = message)
@main.route('/blog/<int:blog_id>')
def blog(blog_id):
    
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('blog.html',id = blog_id)

def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to Blogs'
    return render_template('index.html', title = title)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)