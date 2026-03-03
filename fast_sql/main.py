from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from fast_sql.database import Base, Sessionlocal, engine
from fast_sql.models import Employee, SensorReading


# Intialize the FastAPI app
app = FastAPI(title="FastAPI with SQLAlchemy")

# Create the database tables in pgAdmin automatically when the app starts
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
# Create an employee endpoint to create a new employee in the database
@app.post("/employees/")
def create_employee(name: str, email: str, department: str, db: Session = Depends(get_db)):
    new_employee = Employee(name=name, email=email, department=department)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


@app.post("/sensor_readings/")
def create_sensor_reading(sensor_name: str, timestamp: str, value: float, db: Session = Depends(get_db)):
    new_sensor_reading = SensorReading(sensor_name=sensor_name, timestamp=timestamp, value=value)
    db.add(new_sensor_reading)
    db.commit()
    db.refresh(new_sensor_reading)
    return new_sensor_reading

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy!"}



@app.get("/employees/")
def list_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees