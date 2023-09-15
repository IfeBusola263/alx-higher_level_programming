#!/usr/bin/python3
'''
This Module updates a state object in an SQL DBMS using an ORM
'''


if __name__ == '__main__':
    import sqlalchemy
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from sqlalchemy import (create_engine)

    username = argv[1]
    pwd = argv[2]
    dBase = argv[3]

    # create connection to database with the engine object
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, pwd, dBase))

    # create a custom session factory from the session factory
    Session = sessionmaker(bind=engine)
    # create a session from the session factory
    session = Session()

    # query for the object and update, then commit changes and close session
    state_obj = session.query(State).filter_by(id=2).first()
    state_obj.name = 'New Mexico'
    session.commit()
    session.close()
