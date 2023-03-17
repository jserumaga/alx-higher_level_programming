#!/usr/bin/python3
"""file that contains the class definition of a State
and an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()


class State(Base):
    """ ORM class for state """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states",
                          cascade="all, delete, delete-orphan")
