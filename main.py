from flask import Flask, flash, render_template, request, redirect, url_for, abort
# from flask_mongoengine import MongoEngine
# from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, login_required
# from flask_login import login_user

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Actor

# import os

###### START FLASK APP AND CONNECT TO DATABASE
app = Flask(__name__)
# engine = create_engine('sqlite:///actors.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()


@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

############### ACTOR PAGE
@app.route('/actor/', methods=['GET', 'POST'])
def show_actor_profile():
    return render_template('actorprofile.html')

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

############### DIRECTOR SEARCH PAGE
@app.route('/postjobs/', methods=['GET', 'POST'])
def post_gig():
    return render_template('postjobs.html')

@app.route('/searchactors/')
def search_actors():
    return render_template('searchactors.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
