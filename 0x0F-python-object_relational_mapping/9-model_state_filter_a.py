#!/usr/bin/python3
"""
script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name.like('%a%')).all()
    for state in data:
        print('{}: {}'.format(state.id, state.name))
    session.close()
