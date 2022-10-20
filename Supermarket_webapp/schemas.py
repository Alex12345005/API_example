import email
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
