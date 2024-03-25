from pydantic import BaseModel
from sqlalchemy import Column, Integer, TEXT
from db import DB_Base


class Todo(BaseModel):
    id: int
    todo: str

class TodoTable(DB_Base):
    __tablename__ = "todo"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    todo = Column(TEXT, index=True)



