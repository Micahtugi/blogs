from flask import render_template
from . import main
from .forms import ReviewForm
from ..models import Review
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