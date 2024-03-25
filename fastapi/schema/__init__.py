from pydantic import BaseModel
from typing import List, Optional
from model import Todo


class CreateTodoInput(BaseModel):
    todo: str

class GetAllTodoOutput(BaseModel):
    todos: List[Todo]

class GetTodoOutput(BaseModel):
    todo: Optional[Todo]
