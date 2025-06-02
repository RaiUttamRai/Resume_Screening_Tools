from pydantic import BaseModel,EmailStr
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    recruiter = "recruiter"
    candidate = "candidate"

class UserCreate(BaseModel):
    full_name:str
    email:EmailStr
    password:str
    role: RoleEnum

class UserOut(BaseModel):
    id:int
    full_name:str
    email:EmailStr
    role:RoleEnum
    class Config:
        orm_mode = True
    