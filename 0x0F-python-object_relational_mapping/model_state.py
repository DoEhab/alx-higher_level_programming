#!/usr/bin/python3
"""model_state uses ORM to create table"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class for states table"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
