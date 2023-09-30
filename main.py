from fastapi import FastAPI
from routers import users, certificates
from sql.database import SessionLocal, engine
from sql import models

app = FastAPI()

app.include_router(users.router)
app.include_router(certificates.router)

models.Base.metadata.create_all(bind=engine)


