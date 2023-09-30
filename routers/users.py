from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/users")



router.get("/login")
async def login():
    return 0


router.get("/register")
async def register():
    return 0;