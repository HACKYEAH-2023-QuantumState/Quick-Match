from fastapi import FastAPI
from sql.database import SessionLocal, engine
from sql import models

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


