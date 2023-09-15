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
    inputState = argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, pwd, dBase))

    Session = sessionmaker(bind=engine)
    session = Session()
    position = session.query(State.id).filter(
        State.name.like(f'{inputState}')).order_by(State.id).all()

    if not position:
        print('Not found')
    else:
        for row in position:
            for col in row:
                print(col)
