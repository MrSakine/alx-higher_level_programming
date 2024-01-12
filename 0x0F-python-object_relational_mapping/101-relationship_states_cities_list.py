#!/usr/bin/python3
"""
This module creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
