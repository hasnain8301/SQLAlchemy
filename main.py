from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from datetime import datetime
import os


#  BASE CLASS TO CREATE DATABASE SCHEMA TABLE AND MODLE
Base = declarative_base()


# GET THE PATH OF BASE DIRECTOR IN WHICH YOUR FILE EXIST
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# DEFINE THE CONNECTION STRING WHICH TAKES DATABASE NAME AND PATH -> sqlite:///test.db/
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'test.db')


# DATABASE ENGINE IS CREATED AND READY TO USE - echo=True HELPS USE TO ACKNOWLEDGE THE TASK SUSSEFULLY PERFORMED IN DATABASE
engine = create_engine(connection_string, echo=True)


Session = sessionmaker()

# THIS IS OUR TABLE SCHEMA
"""
USER TABLE SCHEMA

id         : Integer
username   : String
email      : String
created_at : DateTime

"""

# THIS CLASS CREATE 
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username   = Column(String(25),unique=True, nullable=False)
    email      = Column(String(80),unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<{self.id}> | Username: {self.username} | Email: {self.email} | Created on: {self.created_at}"


