#!/usr/bin/python3
'''
This module prints all the city Object in the SQL DB,
through an ORM
'''

if __name__ == '__main__':
    import sqlalchemy
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from sqlalchemy import create_engine

    username = argv[1]
    pwd = argv[2]
    dBase = argv[3]

    # create connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, pwd, dBase))

    Base.metadata.create_all(engine)

    # create a custom session factory
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id==State.id).all()

    for city, state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')
