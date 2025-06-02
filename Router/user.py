# from typing import List
# from fastapi import APIRouter, Depends,status,Reponse,HTTPException
# from .import schemas,models
# from .database import get_db
# from .hashing import Hash
# from sqlalchemy.orm import Session
# from .Repository import user
# from . import oauth2
# router = APIRouter(
#     prefix="/user",
#     tags=["User"]
# )
# @router.get("/",status_code =status.HTTP_201_CREATED)
# def register_user(request:schemas.UserCreate,db:Session= Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
#     return new_user.register_user(request, db)