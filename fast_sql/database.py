from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from pydantic import BaseModel
from typing import Optional , List




# Database setup
# We will use PostgreSQL as our database, you can change it to MySQL or SQLite as per your requirement
# Create our engine to connect to the database
engine = create_engine("postgresql://postgres:T365t14#@localhost:5432/fastapi_db", echo=True)
# Create a session local class to manage our database sessions 
# The benefit of using sessionmaker is to not load the entire database each time we want to interact with it, it will create a new session for us and close it after the interaction is done
# autocommit=False means that we will have to commit our changes to the database manually, this is useful for transactions
# autoflush=False means that the session will not automatically flush changes to the database, this is useful for performance reasons
# bind=engine means that we will use the engine we created to connect to the database
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 
class Base(DeclarativeBase):
    pass
