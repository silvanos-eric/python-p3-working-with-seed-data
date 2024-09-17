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

    # Console message indicating the beginning of the seed operation
    print("Seeding games...")
    games = [
        Game(title=fake.name(),
             genre=fake.word(),
             platform=fake.word(),
             price=random.randint(0, 60)) for i in range(50)
    ]
    print('Done seeding games!')

    session.bulk_save_objects(games)
    session.commit()
