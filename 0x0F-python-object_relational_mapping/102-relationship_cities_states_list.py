#!/usr/bin/python3
'''
This module prints the state and city relationship in a database
through an ORM
'''


if __name__ == '__main__':
    import sqlalchemy
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    username = argv[1]
    pwd = argv[2]
    dBase = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, pwd, dBase))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
