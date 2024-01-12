#!/usr/bin/python3
"""
This module contains the class definition of a City and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City ORM definition

    Attributes:
        - __tablename__ => the name of the table
        - id => the ID of the table columns
        - name => the name of the table colums
        - state_id => the foreign key that represents state table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
