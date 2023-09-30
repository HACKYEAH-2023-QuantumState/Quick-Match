from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/cert")



router.get("/")
async def get():
    return 0

