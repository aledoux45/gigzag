from flask import Flask, Response, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User

app = Flask(__name__)

engine = create_engine('sqlite:///users.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def newUser():
    if request.method == 'POST':
        username = request.form['username']
        if session.query(User).filter_by(username=username).first():
            return render_template('newuser.html', error="Username already exists!")
        newUser = User(username=request.form['username'], password=request.form['password'])
        session.add(newUser)
        session.commit()
        return redirect(url_for('show_user_profile', username=request.form['username']))
    else:
        return render_template('newuser.html', error="")


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if session.query(User).filter_by(username=username).first():
            truepassword = session.query(User).filter_by(email=email).first().password
            if truepassword == password:
                user = User(email, password)
                login_user(user)
                return redirect(url_for('show_user_profile', username=user.username))
        else:
            print("This username does not exist")
            return abort(401)      
    else:
        return render_template('login.html')

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("logout.html")

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return 'Login failed'


# callback to reload the user object        
@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

@login_required    
@app.route('/user/<username>/', methods=['GET', 'POST'])
def show_user_profile(username):
    return render_template('userprofile.html', username=username)



############### DIRECTOR SEARCH PAGE
@app.route('/search/', methods=['GET', 'POST'])
def show_all_actors():
    return render_template('search.html')



if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)