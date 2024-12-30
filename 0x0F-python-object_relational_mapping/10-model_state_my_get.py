#!/usr/bin/python3
"""
print the state id that matches the arg
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """connect to sql using sql alchemy and run select query"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    state_val = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .filter(State.name == state_val)
        .order_by(State.id.asc()).first()
    )

    if states:
        print(states.id)
    else:
        print("Not found")
