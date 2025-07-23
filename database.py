ase.py

import os

#from dotenv import load_dotenv

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

#load_dotenv()

#load the env file

#we can also set these environment variables

DB_USER os.getenv('DB_USER', 'root')

DB_PASS os.getenv('DB_PASS', 'root')

DB_HOST = os.getenv('DB_HOST', 'localhost')

DB_NAME = os.getenv('DB_NAME', 'test_db')

I

#DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

- DATABASE_URL = f"mysql+mysqlconnector://root:root@localhost/test_db"

2

#create the SQLAlchemy engine

engine create_engine (DATABASE_URL, echo True)

#create a configured "Session" class

SessionLocal sessionmaker (autocommit=False, autoflush False, bind=engine)

Base declarative_base()
