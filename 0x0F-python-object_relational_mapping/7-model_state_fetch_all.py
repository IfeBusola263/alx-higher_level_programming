#!/usr/bin/python3
'''
This module prints all the states in the database using an ORM
'''

if __name__ == '__main__':
    from model import Base, State
    from sys import argv
    import sqlalchemy
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    pwd = argv[2]
    dBase = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:\
    3306/{}".format(username, pwd, dBase))

    session = Session(sessionmaker(bind=engine))
    states = session.query(State).all()

    for state in states:
        print(f'{state.id}: {state.name}')
