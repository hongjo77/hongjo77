from fastapi import APIRouter, FastAPI
from typing import List, Optional

from model import Todo
from schema import *

router = APIRouter(
    prefix="",
    tags=["ㅎㅇ"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return "dd"
