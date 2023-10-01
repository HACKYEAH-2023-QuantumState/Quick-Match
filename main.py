import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import survey, admin
from sql.database import SessionLocal, engine
from sql import models
from test.populate_db import populate
import os

os.remove("sql_app.db")

app = FastAPI()


origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(survey.router)
app.include_router(admin.router)

populate(10, 20)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
