#!/usr/bin/python3
'''
This is a module for creating a cities table (Schema)
 in DBMS through an ORM
'''


# if __name__ == '__main__':
from model_state import Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''
    The city class inherits from the Base declarative class,
    to aid instrumentation of the City class and also possibility of
    mapping each cities instance to a DBMS.
    '''
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
