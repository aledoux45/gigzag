import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import UserMixin

Base = declarative_base()

# class User(UserMixin, Base):
#     __tablename__ = 'user'

#     username = Column(String(50), primary_key=True)
#     password = Column(String(50), nullable=False)

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password


from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
