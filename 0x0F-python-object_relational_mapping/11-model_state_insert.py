#!/usr/bin/python3
'''
This module adds a new state to the existing database with ORM
'''


if __name__ == '__main__':
    import sqlalchemy
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from sys import argv

    username = argv[1]
    pwd = argv[2]
    dBase = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, pwd, dBase))

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    new_state_id = session.query(State.id).filter(
        State.name.like('Louisiana')).all()

    if new_state_id:
        for row in new_state_id:
            for col in row:
                print(col)

    session.close()
