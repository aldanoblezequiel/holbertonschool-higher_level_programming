#!/usr/bin/python3
"""Cities from the Dbase"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    new = State(name='California', cities=[City(name='San Francisco')])
    session.add(new)
    session.commit()

    session.close()
