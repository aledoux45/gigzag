from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Actor

import os

###### START FLASK APP AND CONNECT TO DATABASE
app = Flask(__name__)
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def home():
    return render_template('indexbulma.html', error="")


@app.route('/user/<username>/', methods=['GET', 'POST'])
def show_user_profile(username):
    return render_template('userprofile.html', username=username)


############### DIRECTOR SEARCH PAGE
@app.route('/search/', methods=['GET', 'POST'])
def show_all_actors():
    # actors = User.query.all()
    return render_template('search.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
