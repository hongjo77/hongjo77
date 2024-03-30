from pydantic import BaseModel
from sqlalchemy import Column, Integer, TEXT,create_engine,Float,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from db import DB_Base

class ParentTable(DB_Base):
    __tablename__ = "parent"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,index=True)
    email = Column(String,index=True)
    password = Column(String,index=True)

    todos = relationship("TodoTable", back_populates="parent",viewonly=True)


