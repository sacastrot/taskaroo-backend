"""
This module contains the database configuration and session management. In this module,
we define the SQLAlchemy engine, session, and base class for the database models.
We also define the database URL in the config module and import it here to create the engine.
"""


# Standard library imports
import os
from os.path import join, dirname

# Third-party imports
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

db_name = os.getenv("DATABASE_NAME")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_host = os.getenv("DATABASE_HOST")
db_port = os.getenv("DATABASE_PORT")


# The database URL is in the format "dialect+driver://username:password@host:port/database"
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the database models
Base = declarative_base()
