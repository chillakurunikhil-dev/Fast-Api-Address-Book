from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models
from schemas import AddressCreate, AddressUpdate, AddressOut
from utils import calculate_distance

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses/", response_model=AddressOut)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    new_address = models.Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


@app.get("/addresses/", response_model=list[AddressOut])
def get_addresses(db: Session = Depends(get_db)):
    return db.query(models.Address).all()


@app.put("/addresses/{address_id}", response_model=AddressOut)
def update_address(address_id: int, data: AddressUpdate, db: Session = Depends(get_db)):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    address.name = data.name
    address.latitude = data.latitude
    address.longitude = data.longitude

    db.commit()
    db.refresh(address)
    return address


@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    db.delete(address)
    db.commit()
    return {"message": "Address deleted"}


@app.get("/addresses/nearby", response_model=list[AddressOut])
def get_nearby(lat: float, lon: float, distance_km: float, db: Session = Depends(get_db)):
    all_addresses = db.query(models.Address).all()
    result = []

    for addr in all_addresses:
        dist = calculate_distance(lat, lon, addr.latitude, addr.longitude)
        if dist <= distance_km:
            result.append(addr)

    return result