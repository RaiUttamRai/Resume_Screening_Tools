from fastapi impott APIRouter,Depends,status,Response,HTTPException
from typing import List
from sqlalchemy.orm import Session
from . import schemas,models
from .database import get_db

def get_all_user(db:Session):
    users= db.query(models.User).all()
    return users

def register_user(request:schemas.UserCreate, db:Session):
    new_user = models.User(
        full_name = request.full_name,
        email = request.email,
        hashed_password = request.password,
        role = request.role

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    )