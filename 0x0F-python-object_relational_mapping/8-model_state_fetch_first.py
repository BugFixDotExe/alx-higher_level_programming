#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This moudle is meant to print
the first State object from the
database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    for state in session.query(State).order_by(State.id)[:1]:
        print("{}: {}".format(state.id, state.name))
    session.close()
