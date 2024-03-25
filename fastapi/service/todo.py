from fastapi import APIRouter, FastAPI
from typing import List, Optional

from model import TodoTable
from schema import *
from db import get_db_session


class TodoService:
    def __init__(self):
        self.model=Todo

    def getAll(self) -> List[TodoTable]:
        db=get_db_session()
        try:
            todo = db.query(TodoTable).all()
            return todo
        
        except Exception as e:
            raise Exception(e)

        return True

    def getOne(self, todo_id: int) -> Optional[Todo]:
        db=get_db_session()
        try:
            todo = db.query(TodoTable).filter(TodoTable.id==todo_id).first()
            if todo is None:
                return None

            return todo
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")

    def createOne(self,todo: str):
        db=get_db_session()
        try:
            todo = TodoTable(todo=todo)
            db.add(todo)
            db.commit()
            db.refresh(todo)

            return True
        except Exception as e:
            db.rollback()
            raise Exception(e)

    def putOne(self, todo_id: int, todostr: str) -> bool:
        db=get_db_session()
        try:
            todo = db.query(TodoTable).filter(TodoTable.id==todo_id).first()
            if todo is None:
                return False
            
            setattr(todo, "todo", todostr)
    
            db.commit()

            return True
        except Exception as e:
            db.rollback()
            raise Exception(e)

    def delOne(self, todo_id: int)-> bool:
        db=get_db_session()
        try:
            todo = db.query(TodoTable).filter(TodoTable.id==todo_id).first()
            if todo is None:
                return False
            db.delete(todo)
            db.commit()

            return True
        except Exception as e:
            db.rollback()
            raise Exception(e)
            
