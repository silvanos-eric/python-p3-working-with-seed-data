#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':

    # Create an engine for the database
    engine = create_engine('sqlite:///seed_db.db')
    # Configure sessionmaker to use the engine
    Session = sessionmaker(bind=engine)
    # Create a new session
    session = Session()
    # Drop Game table
    session.query(Game).delete()
    session.commit()

    # in-memory instances
    botw = Game(title="Breath of the Wild",
                platform="Switch",
                genre="Adventure",
                price=60)
    ffvii = Game(title="Final Fantasy VII",
                 platform="Playstation",
                 genre="RPG",
                 price=30)
    mk8 = Game(title="Mario Kart 8",
               platform="Switch",
               genre="Racing",
               price=50)
    ccs = Game(title="Candy Crush Saga",
               platform="Mobile",
               genre="Puzzle",
               price=0)

    session.bulk_save_objects([botw, ffvii, mk8, ccs])
    session.commit()
