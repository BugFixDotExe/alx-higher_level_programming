#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module demonstrates the class definition of a State
and an instance Base = declarative_base()
It searves as the shema for how the database columns
will be created in the database
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


class State(Base):
    """
    A state class that acts as the template for creating or the
    schema to the database columns
    Args:
        Base (Base obj): A Base object
    """
    __tablename__ = 'states'
    id = Column(Integer(),
                autoincrement=True,
                primary_key=True,
                nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)


# create all tables
Base.metadata.create_all(engine)
session = Session()
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
