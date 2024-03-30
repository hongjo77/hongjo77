from fastapi import APIRouter, FastAPI, HTTPException

from schema import *
from schema.todo import *

from service.todo import TodoService
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

todoService = TodoService()

@router.post("/parent")
async def root(data: CreateTodoInput):
    todo = todoService.createTodo(data)

    return {"parent" : todo}

@router.get("/todo/user/{input}")
async def root(input: int):
    p=GetUserTodosInput(id=input)
    todo = todoService.getUserTodos(p)

    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    
    return todo

@router.get("/todo/id/{input}")
async def root(input: int):
    p=GetTodoByIdInput(id=input)
    todo = todoService.getTodoById(p)

    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    
    return todo
