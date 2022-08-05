#!/usr/bin/python3
"""Cities from Dbase"""

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

    busquedas = session.query(State).order_by(State.id).all()

    for row in busquedas:
        print("{}: {}".format(row.id, row.name))
        for city in row.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
