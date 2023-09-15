#!/usr/bin/python3
'''
This module interacts with database(MYSQL) using an ORM(SQLAlchemy)
'''


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine


Base = declarative_base()


class State(Base):
    '''
    the state class inherits from base class, which helps
    in describing the database's table we are interacting with
    and also functionality to help us map our object to the table,
    and the attributes to the column of the databases table. This is
    called instrumentation.
    '''

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128))
