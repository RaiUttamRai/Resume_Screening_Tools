# from fastapi import Depends,status,Response,HTTPException
# from typing import List
# from sqlalchemy.orm import Sesssion
# from fastapi.security import OAuth2PasswordRequestForm
# from .import schemas,models,Token
# from .database import get_db
# from .hashing import Hash

# router = APIRouter(
#     prefix="/auth",
#     tags=["Authentication"],
# )
# @router.post("/",status_code=status.HTTP_201_OK)
# def login(user:Oauth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
#     db_user = db.query(models.User).filter(models.User.email==user.username).first()
#     if not db_user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Invlid Credentials"
#         )
#     if not Encrypt.verify(user.password, db_user.password):
#         raise HTTPException(
#             status_code= status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect Password",
#         )
#         access_token = Token.create_access_token(data={"sub":db_user.email})
#         return{"access_token": access_token, "token_type": "bearer"}