from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from carparkAPI import crud, models, schemas
from carparkAPI.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

#API
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.head("/v1/")
async def root():
    return {"message": "Hello World"}

############## Manufacturer ##################
@app.post("/v1/manufacturer/", response_model=schemas.Manufacturer)
def create_manufacturer(manufacturer: schemas.ManufacturerCreate, db: Session = Depends(get_db)):
    db_manufacturer = crud.get_manufacturer_by_name(db, manufacturer_name=manufacturer.name)
    if db_manufacturer:
        raise HTTPException(status_code=400, detail="Manufacturer already exists")
    return crud.create_manufacturer(db=db, manuf=manufacturer)

@app.get("/v1/manufacturer/{manufacturer_id}", response_model=schemas.Manufacturer)
def read_manufacturer(manufacturer_id: int, db: Session = Depends(get_db)):
    db_manufacturer = crud.get_manufacturer(db, manufacturer_id=manufacturer_id)
    if db_manufacturer == None:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return db_manufacturer

@app.get("/v1/manufacturer/", response_model=list[schemas.Manufacturer])
def read_manufacturers(db: Session = Depends(get_db)):
    db_manufacturers = crud.get_manufacturers(db)
    if db_manufacturers == None:
        raise HTTPException(status_code=400, detail="No manufacturer available")
    return db_manufacturers

############## Cars ##################
@app.post("/v1/cars/", response_model=schemas.Cars)
def create_car(car: schemas.CarsCreate, db: Session = Depends(get_db)):
    db_cars=crud.get_car_by_numberplate(db, numberplate=car.numberplate)
    if db_cars:
        raise HTTPException(status_code=400, detail="Numberplate already exists")
    return crud.create_car(db=db, car=car, manufacturer_id=car.manufacturer_id, numberplate=car.numberplate)



@app.get("/v1/cars/{car_id}", response_model=schemas.Cars)
def read_cars(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id=car_id)
    if db_car == None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@app.get("/v1/cars/", response_model=list[schemas.Cars])
def read_all_cars(db: Session = Depends(get_db)):
    db_cars = crud.get_cars(db)
    if db_cars == None:
        raise HTTPException(status_code=404, detail="No Cars not found")
    return db_cars


############## Customers ##################



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)