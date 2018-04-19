import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Actor(Base):
    __tablename__ = 'actor'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'id': self.id,
        }


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)