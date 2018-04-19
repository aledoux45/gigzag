import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import UserMixin

Base = declarative_base()

class User(UserMixin, Base):
    __tablename__ = 'user'

    username = Column(String(50), primary_key=True)
    password = Column(String(50), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    dateofbirth = Column(String(250), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
