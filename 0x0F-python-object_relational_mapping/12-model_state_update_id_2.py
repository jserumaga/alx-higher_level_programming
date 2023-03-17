
#!/usr/bin/python3
"""
script that changes the name of a State object
from the database hbtn_0e_6_usa
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

    change_state = session.query(State).filter(State.id == 2).first()
    if change_state:
        change_state.name = "New Mexico"

    session.commit()
    session.close()
