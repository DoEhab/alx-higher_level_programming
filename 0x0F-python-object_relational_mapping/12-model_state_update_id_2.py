#!/usr/bin/python3
"""
Update state name where id =2
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
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})

    session.commit()
    session.close()
