#!/usr/bin/python3
'''
This module creates a new object on two tables using relationships
through a DBAPI(MySqlDB) and an ORM(SqlAlchemy)
'''


if __name__ == '__main__':
    import sqlalchemy
    from sqlalchemy import create_engine
    from relationship_city import City
    from relationship_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    username = argv[1]
    pwd = argv[2]
    dBase = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, pwd, dBase))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name="San Francisco")
    new_city.state = State(name='California')
    session.add(new_city)
    session.commit()
    session.close()
