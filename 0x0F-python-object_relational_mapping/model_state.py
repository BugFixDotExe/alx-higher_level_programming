#!/usr/bin/python3
"""
 a python file that contains,
 the class definition of a State
 and an instance Base = declarative_base()
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

# Declare class here
class State(Base):

    __tablename__ = 'states'
    id = Column(Integer(),
                autoincrement=True,
                primary_key=True,
                nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
# Class declaration end here


# create all tables
Base.metadata.create_all(engine)
session = Session()
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
