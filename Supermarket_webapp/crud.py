from sqlalchemy.orm import Session

from . import models, schemas
import logging


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.hashed_password
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products_by_name(db: Session, name: str):
    logging.error("got parameter %s" ,name)
    if name != "":
        result_set = db.query(models.Product).filter(models.Product.name == name).all()
        return result_set
    return db.query(models.Product).all()

def get_product_by_id(db: Session, id: str):
    logging.info("got parameter %s" ,id)
    if id != "":
        result_set = db.query(models.Product).filter(models.Product.id == id).first()
        return result_set
    return db.query(models.Product).all()


def get_product(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, description = product.description,
                                price = product.price, id = product.id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_cart_item(db: Session, cart_item: schemas.CartItemCreate):
    db_cartitem = models.CartItem(user_id=cart_item.user_id, product_barcode = cart_item.product_barcode,
                                quantity = cart_item.quantity)
    db.add(db_cartitem)
    db.commit()
    db.refresh(db_cartitem)
    return db_cartitem

def get_cart_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CartItem).offset(skip).limit(limit).all()
