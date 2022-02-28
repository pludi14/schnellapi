from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

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





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)