from fastapi import FastAPI

from routers import survey
from sql.database import SessionLocal, engine
from sql import models

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(survey.router)

