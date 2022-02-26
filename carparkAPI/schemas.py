from pydantic import BaseModel


class CarsBase(BaseModel):
    name: str
    tyres: int
    doors: int
    horsepower: int
    type= str


class CarsCreate(CarsBase):
    manufacturer_id=int
    pass

class Cars(CarsBase):
    id: int
    manufacturer_id: int

    class Config:
        orm_mode = True

####################################

class ManufacturerBase(BaseModel):
    name: str
    location: str

class ManufacturerCreate(ManufacturerBase):
    pass

class Manufacturer(ManufacturerBase):
    id: int
    cars: list[Cars] =[]

    class Config:
        orm_mode = True


#################################


class CustomersBase(BaseModel):
    name: str

class CustomersCreate(CustomersBase):
    pass

class Customers(CustomersBase):
    status: bool
    cars: list[Cars] = []

    class Config:
        orm_mode = True
