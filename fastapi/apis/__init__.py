from fastapi import APIRouter, FastAPI

from schema import *

router = APIRouter(
    prefix="",
    tags=["ㅎㅇ"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return "dd"
