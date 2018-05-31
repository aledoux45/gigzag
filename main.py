from flask import Flask, flash, render_template, request, redirect, url_for, abort
from flask_mongoengine import MongoEngine, Document
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, InputRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import config
import sys

app = Flask(__name__)

db = MongoEngine(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Document):
    meta = {'collection': 'actors'}
    email = db.StringField(max_length=30)
    password = db.StringField()

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

class RegForm(FlaskForm):
    firstname = StringField('firstname',  validators=[InputRequired(), Length(max=100)])
    lastname = StringField('lastname',  validators=[InputRequired(), Length(max=100)])
    username = StringField('username',  validators=[InputRequired(), Length(min=8, max=25)])
    phone = StringField('phone',  validators=[InputRequired(), Length(10)])
    union = StringField('union',  validators=[InputRequired(), Length(max=100)])
    email = StringField('email',  validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=25)])


############### HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            existing_user = User.objects(email=form.email.data).first()
            if existing_user is None:
                hashpass = generate_password_hash(form.password.data, method='sha256')
                hey = User(form.email.data,hashpass).save()
                login_user(hey)
                return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('dashboard'))
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            check_user = User.objects(email=form.email.data).first()
            if check_user:
                if check_password_hash(check_user['password'], form.password.data):
                    login_user(check_user)
                    return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

############### ACTING PAGE
# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', name=current_user.email)

@app.route('/actor/', methods=['GET', 'POST'])
@login_required
def show_actor_profile():
    return render_template('actorprofile.html', name=current_user.email)

@app.route('/jobswall/', methods=['GET', 'POST'])
def show_jobs_wall():
    return render_template('jobswall.html')

@app.route('/skills/language/', methods=['GET', 'POST'])
def skills_language():
    return render_template('skills_language.html')

@app.route('/skills/sport/', methods=['GET', 'POST'])
def skills_sport():
    return render_template('skills_sport.html')

@app.route('/skills/acting/', methods=['GET', 'POST'])
def skills_acting():
    return render_template('skills_acting.html')

@app.route('/skills/measurements/', methods=['GET', 'POST'])
def skills_measurements():
    return render_template('skills_measurements.html')

@app.route('/skills/other/', methods=['GET', 'POST'])
def skills_other():
    return render_template('skills_other.html')

@app.route('/skills/experience/', methods=['GET', 'POST'])
def skills_experience():
    return render_template('skills_experience.html')

############### CASTING PAGE
@app.route('/postjobs/', methods=['GET', 'POST'])
def post_gig():
    return render_template('postjobs.html')

@app.route('/searchactors/')
def search_actors():
    return render_template('searchactors.html')


if __name__ == "__main__":
    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
    
    if env == 'dev':
        app.config = config.DevelopmentConfig
    elif env == 'test':
        app.config = config.TestConfig
    elif env == 'prod':
        app.config = config.ProductionConfig
    else:
        raise ValueError('Invalid environment name')

    app.run(host='0.0.0.0', port=8080)

