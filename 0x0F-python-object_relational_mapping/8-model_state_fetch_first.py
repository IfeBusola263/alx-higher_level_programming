#!/usr/bin/python3
'''
This module prints all the states in the database using an ORM
'''

if __name__ == '__main__':
    from model_state import Base, State
    from sys import argv
    import sqlalchemy
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    pwd = argv[2]
    dBase = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, pwd, dBase))

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    check = state.all()

    if check:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')
