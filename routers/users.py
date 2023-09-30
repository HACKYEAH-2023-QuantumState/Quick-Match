from fastapi import APIRouter, Depends, HTTPException
from sql import schemas
from sql.database import get_db


import sql.crud

router = APIRouter(prefix="/users")


@router.post("/login", response_model=schemas.User)
async def login():
    return 0;


@router.post("/register", response_model=schemas.User)
async def register(user: schemas.UserCreate, db=Depends(get_db)):
    return sql.crud.create_user(db, user)
