from fastapi import APIRouter, FastAPI

from model.parent import ParentTable
from model.todo import TodoTable

from schema import *
from schema.todo import *
from db import get_db_session


class TodoService:

    def createTodo(self, p: CreateTodoInput) -> CreateTodoOutput:
        db=get_db_session()
        try:
            todo = TodoTable(parent_id=p.parent_id, title=p.title,content=p.content)
            db.add(todo)
            db.commit()
            db.refresh(todo)

            return todo
        except Exception as e:
            db.rollback()
            raise Exception(e)
        
    def getUserTodos(self, p: GetUserTodosInput) -> GetUserTodosOutput:
        db=get_db_session()
        try:
            todo = db.query(TodoTable).filter(ParentTable.id==p.id).all()
            if todo is None:
                return None

            return todo
        except Exception as e:
            #raise HTTPException(status_code=500, detail="Internal server error")
            raise Exception(e)
        
    def getTodoById(self, p: GetTodoByIdInput) -> GetTodoByIdOutput:
        db=get_db_session()
        try:
            todo = db.query(TodoTable).filter(TodoTable.id==p.id).first()
            if todo is None:
                return None

            return todo
        except Exception as e:
            #raise HTTPException(status_code=500, detail="Internal server error")
            raise Exception(e)
