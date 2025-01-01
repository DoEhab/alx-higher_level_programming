#!/usr/bin/python3
"""model_state uses ORM to create table"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).all()

    for row in all_states:
        print(f"{row.id}: {row.name}")