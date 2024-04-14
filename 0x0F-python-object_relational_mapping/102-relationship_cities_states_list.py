#!/usr/bin/python3
"""A script that lists all City objects from the database hbtn_0e_101_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.schema import Table

if __name__ == "__main__":

    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
engine = create_engine(conn_str.format(db_username, db_password, db_name), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
cities = session.query(City).order_by(City.id).all()
for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
