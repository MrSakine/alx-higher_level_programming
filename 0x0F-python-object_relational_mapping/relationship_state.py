#!/usr/bin/python3
"""
This module contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State ORM definition

    Attributes:
        - __tablename__ => the name of the table
        - id => the ID of the table columns
        - name => the name of the table colums
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
    )
