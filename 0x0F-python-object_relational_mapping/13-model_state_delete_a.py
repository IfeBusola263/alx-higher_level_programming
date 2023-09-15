#!/usr/bin/python3
'''
This module deletes all states in the database with letter "a"
from a mysql DBMS using an ORM for the query.
'''


if __name__ == '__main__':
    import sqlalchemy
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv

    username = argv[1]
    pwd = argv[2]
    dBase = argv[3]

    # create connection with dababase using the dbAPIcore and ORM
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, pwd, dBase))

    # create custom session factory
    Session = sessionmaker(bind=engine)
    # create session to start conversation with DBMS
    session = Session()

    to_del = session.query(State).filter(State.name.like('%a%')).all()

    for obj in to_del:
        session.delete(obj)

    session.commit()
    session.close()
