from sqlalchemy import Column, Integer, String, Float
from fast_sql.database import Base

# Define our Employee model which will be used to create the users table in the database
class Employee(Base):
    __tablename__ = "employees" # This is the name of the table in the database
    id = Column(Integer, primary_key=True, index=True) # This is the primary key of the table, it will be auto-incremented
    name = Column(String, index=True) # This is the name of the employee, it will be indexed for faster queries
    email = Column(String, unique=True, index=True) # This is the email of the employee, it will be unique and indexed for faster queries
    department = Column(String, index=True) # This is the department of the employee, it will be indexed for faster queries

class SensorReading(Base):
    __tablename__ = "sensor_readings"
    id = Column(Integer, primary_key=True, index=True)
    sensor_name = Column(String, index=True)
    timestamp = Column(String, index=True)
    value = Column(Float, index=True)