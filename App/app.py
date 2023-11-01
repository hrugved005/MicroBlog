from App import app
from flask import render_template, flash, redirect, url_for
from App.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Hrugved'}
    posts= [
        {'author':{'username':'Danish'}, 'body':'Acchi baat Hai'},
        {'author':{'username':'Manas'}, 'body':'If you dont cum for a week, the residual sperm is sourced to your mind.'}
    ]
    return render_template('index.html', title='MicroBlog', user=user, posts=posts)

@app.route('/info')
def info():
    return'<h1>About Page</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)