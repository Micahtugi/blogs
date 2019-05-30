from flask import render_template
from app import app

# Views
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