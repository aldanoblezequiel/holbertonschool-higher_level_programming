#!/usr/bin/python3
"""Listing state objects from the Dbase"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
