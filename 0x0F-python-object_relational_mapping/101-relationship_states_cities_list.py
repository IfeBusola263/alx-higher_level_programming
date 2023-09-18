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

    states_and_cities = session.query(
        State).join(City).order_by(State.id, City.id).all()

    # print (states_and_cities)
    for state in states_and_cities:
        print(f'{state.id}: {state.name}')

        for site in state.cities:
            print(f'\t{site.id}: {site.name}')
