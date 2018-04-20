from flask import Flask, Response, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from forms import LoginForm, RegistrationForm

from flask_wtf.csrf import CSRFProtect
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import os

###### START FLASK APP
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess',
    WTF_CSRF_SECRET_KEY="a csrf secret key",
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
))


# Database
db = SQLAlchemy(app)
# db.init_app(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


db.create_all()

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

# CSRF Securtity
csrf = CSRFProtect(app)
# csrf.init_app(app)



@app.route('/')
def home():
    return render_template('home.html', error="")

# @app.route('/newuser', methods=['GET', 'POST'])
# def newUser():
#     if request.method == 'POST':
#         username = request.form['username']
#         if session.query(User).filter_by(username=username).first():
#             return render_template('newuser.html', error="Username already exists!")
#         newUser = User(username=request.form['username'], password=request.form['password'])
#         session.add(newUser)
#         session.commit()
#         return redirect(url_for('show_user_profile', username=username))
#     else:
#         return render_template('newuser.html', error="")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# somewhere to login
@app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if session.query(User).filter_by(username=username).first():
#             truepassword = session.query(User).filter_by(username=username).first().password
#             if truepassword == password:
#                 user = User(username, password)
#                 login_user(user)
#                 return redirect(url_for('show_user_profile', username=user.username))
#             else:
#                 return render_template('login.html', error="Wrong password") 
#         else:
#             return render_template('login.html', error="This username does not exist") 
#     else:
#         return render_template('login.html')

def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = session.query(User).filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return 'Login failed'


# callback to reload the user object        
@login_manager.user_loader
def load_user(username):
    return User.query.get(int(id))

 
@app.route('/user/<username>/', methods=['GET', 'POST'])
@login_required   
def show_user_profile(username):
    return render_template('userprofile.html', username=username)



############### DIRECTOR SEARCH PAGE
@app.route('/search/', methods=['GET', 'POST'])
def show_all_actors():
    actors = User.query.all()
    return render_template('search.html', actors=actors)


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
