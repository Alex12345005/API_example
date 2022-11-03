from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import logging

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered!")
    return crud.create_user(db=db, user=user)


@app.get("/users/{users_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    return db_user

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_products_by_name(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Product already in stock!")
    return crud.create_product(db=db, product=product)

@app.get("/products")
async def read_products(name:str = "",  db: Session = Depends(get_db)):
    db_products = crud.get_products_by_name(db, name)
    if db_products is None:
        raise HTTPException(status_code=404, detail="Product not found!")
    return db_products
    
@app.get("/products/{id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found!")
    return db_product