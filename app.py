from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Actor

import os

###### START FLASK APP AND CONNECT TO DATABASE
app = Flask(__name__)
engine = create_engine('sqlite:///actors.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


############### ACTOR PAGE
@app.route('/actor/', methods=['GET', 'POST'])
def show_actor_profile():
    return render_template('actorprofile.html')


@app.route('/jobswall/', methods=['GET', 'POST'])
def show_jobs_wall():
    return render_template('jobswall.html')


############### DIRECTOR SEARCH PAGE
@app.route('/postgig/', methods=['GET', 'POST'])
def post_gig():
    return render_template('postgig.html')

@app.route('/searchactors/')
def search_actors():
    return render_template('searchactors.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
