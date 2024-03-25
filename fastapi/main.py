from fastapi import FastAPI
from typing import List, Optional

from model import Todo
from schema import *
from apis.todo import router as todoRouter
from apis import router as DefaultRouter


app = FastAPI()
app.include_router(DefaultRouter)
app.include_router(todoRouter)









