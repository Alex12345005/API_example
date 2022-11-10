import sqlalchemy
from email.mime import base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import SQLALCHEMY_DATABASE_URL, Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    user_cart_items = relationship("CartItem")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)
    price = Column(Integer, unique=True, index=True)
    barcode = Column(Integer, unique=True, index=True)

class CartItem(Base):
    """cart item representation."""

    __tablename__ = "cartitem"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    product_barcode = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("products.barcode"))
    quantity = sqlalchemy.Column(sqlalchemy.Integer)