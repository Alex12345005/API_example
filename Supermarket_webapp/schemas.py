#import email
from pydantic import BaseModel


class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    email: str
    hashed_password: str

class User(UserBase):
    id: int
    email : str
    
    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    pass

class ProductCreate(ProductBase):
    name: str
    description: str
    price: int
    barcode: int

class Product(ProductBase):
    id: int
    name : str
    description: str
    price: int
    barcode: int
    
    class Config:
        orm_mode = True

class CartItemBase(BaseModel):
    pass

class CartItemCreate(CartItemBase):
    user_id: int
    product_barcode: int
    quantity: int


class CartItem(CartItemBase):
    user_id: int
    product_barcode: int
    quantity: int
    
    class Config:
        orm_mode = True