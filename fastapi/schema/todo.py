from pydantic import BaseModel
from typing import List, Optional
from model.types.todo import Todo

class CreateTodoInput(BaseModel):
    parent_id : int
    title : str
    content : str

class CreateTodoOutput(BaseModel):
    todo : Todo

class GetUserTodosInput(BaseModel):
    id:int

class GetUserTodosOutput(BaseModel):
    todos: Optional[List[Todo]]

class GetTodoByIdInput(BaseModel):
    id:int

class GetTodoByIdOutput(BaseModel):
    todos: Optional[Todo]