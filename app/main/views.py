from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile
from .. import db
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
    return render_template("profile/profile.html", form =form)