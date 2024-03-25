from fastapi import APIRouter, FastAPI, HTTPException
from typing import List, Optional

from model import Todo
from schema import *
from service.todo import TodoService

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

todoService = TodoService()

@router.get("/")
async def root() -> GetAllTodoOutput:
    todos = todoService.getAll()
    if len(todos)==0:
        raise HTTPException(status_code=404, detail="todos not found")
    return {"todos": todos}

@router.get("/{todo_id}")
async def root(todo_id: int) -> GetTodoOutput:
    todo = todoService.getOne(todo_id)
    
    return {"todo": todo} if todo else {"todo": None}


@router.post("/create")
async def root(todo: str):
    todoService.createOne(todo)
    return {"message": "ok"}

@router.put("/{todo_id}")
async def root(todo_id: int, qq: str):
    todoService.putOne(todo_id, qq)

@router.delete("/{todo_id}")
async def root(todo_id: int):
    todoService.delOne(todo_id)