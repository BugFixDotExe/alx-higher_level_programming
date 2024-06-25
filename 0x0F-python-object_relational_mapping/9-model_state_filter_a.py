#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This script is meant to
lists all State objects
that contain the letter a
from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Engine and session creation and initialization begin here
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    # Engine and session creation and initializaiton ends here

    # Database Query begins here
    state = session.query(State).filter(State.name.like('%a%'))[:4]
    if state:
        for record in state:
            print("{}: {}".format(record.id, record.name))
    else:
        print("Nothing")
    session.close()
