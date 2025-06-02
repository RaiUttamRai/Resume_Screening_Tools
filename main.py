from fastapi import FastAPI
from models import Models
from database import engine


app = FastAPI()
Models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}