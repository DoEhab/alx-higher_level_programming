#!/usr/bin/python3
"""model_state uses ORM to create table"""
import sys
from tokenize import String

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = (
        session.query(City, State)
        .join(State, City.id == State.id)
        .order_by(City.id.asc())
        .all()
    )

    for city, state in all_cities:
        print(f"{state.name}:({city.id}) {city.name}")

    session.close()
