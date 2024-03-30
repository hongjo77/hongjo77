from pydantic import BaseModel
from sqlalchemy import func,Column, Integer, TEXT,create_engine,Float,String,ForeignKey,Boolean,TIMESTAMP
from sqlalchemy.orm import relationship
from db import DB_Base

class TodoTable(DB_Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey("parent.id",ondelete='SET NULL'))
    create_time = Column(TIMESTAMP, index=True, default=func.now())
    title = Column(String,index=True)
    content = Column(String,index=True)
    
    parent = relationship("ParentTable", back_populates="todos",viewonly=True)