from flask import render_template, url_for, flash, redirect
from fl_blog import app, db, bcrypt
from fl_blog.forms import RegistrationForm, LoginForm
from fl_blog.models import User, Post


posts = [
    {
        'title':'Excalibur',
        'date_posted':'11-12-2019',
        'author':'Ihor Udod'
    },
    {
        'title':'Excalibur',
        'date_posted':'11-12-2019',
        'author':'Ihor Udod'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts )

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account is created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your Username and Password.', 'danger')
    return render_template('login.html', title='Login', form=form)