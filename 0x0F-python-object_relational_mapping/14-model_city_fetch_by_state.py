#!/usr/bin/python3
"""Cities from the Dbase"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    citis = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in citis:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
