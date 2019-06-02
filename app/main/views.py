from flask import render_template
from app import app
from .models import reviews
from .forms import ReviewForm
Review = review.Review
# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Blogs'
    return render_template('index.html',message = message)
@app.route('/blog/<int:blog_id>')
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