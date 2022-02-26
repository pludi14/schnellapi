from sqlalchemy.orm import Session

from . import models, schemas


##### Cars #####
def get_car(db: Session, car_id: int):
    return db.query(models.Cars).filter(models.Cars.id == car_id).first()

def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cars).offset(skip).limit(limit).all()

def create_car(db: Session, car: schemas.CarsCreate, manufacturer_id: int):
    db_car= models.Cars(name=car.name, tyres=car.tyres, doors=car.doors, horsepower=car.horsepower, type=car.type, manufacturer_id=manufacturer_id)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

##### Manufacturer ####
def get_manufacturer(db: Session, manufacturer_id: int):
    return db.query(models.Manufacturer).filter(models.Manufacturer.id == manufacturer_id).first()

def get_manufacturer_by_name(db: Session, manufacturer_name: str):
    return db.query(models.Manufacturer).filter(models.Manufacturer.name == manufacturer_name).first()

def get_manufacturers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Manufacturer).offset(skip).limit(limit).all()

def create_manufacturer(db: Session, manuf: schemas.ManufacturerCreate):
    db_manuf= models.Manufacturer(name=manuf.name, location=manuf.location)
    db.add(db_manuf)
    db.commit()
    db.refresh(db_manuf)
    return db_manuf


##### Customers ####
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customers).filter(models.Customers.id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customers).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: schemas.CustomersCreate):
    db_customer= models.Customers(name=customer.name, status=customer.status)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer







