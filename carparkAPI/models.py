from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

#Models

class Cars(Base):
    __tablename__="cars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    tyres = Column(Integer)
    doors = Column(Integer)
    horsepower = Column(Integer)
    type=Column(String)
    manufacturer_id = Column(Integer, ForeignKey("manufacturer.id"))

    manufacturer = relationship("Manufacturer", back_populates="cars")
    customers=relationship("Customers", back_populates="cars")


class Manufacturer(Base):
    __tablename__="manufacturer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)

    cars = relationship("Cars", back_populates="manufacturer")


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    status=Column(Boolean, default=False)

    cars=relationship("Cars", back_populates="customers")