#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This moudle is meant to print
the contents of a databse in
ascending order
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
    for state in session.query(State).order_by(State.id)[:5]:
        if (state):
            print("{}: {}".format(state.id, state.name))
        else:
            break
    session.close()
