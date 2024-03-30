from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from sqlalchemy import func,Column, Integer, Text,String ,ForeignKey, TIMESTAMP # TEXT 대신 Text를 사용합니다.
from sqlalchemy.orm import relationship

from core.env import Env
from db import *

SessionLocal = create_db_sessionLocal()
DB_Base = declarative_base()

class ParentTable(DB_Base):
    __tablename__ = "parent"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255),index=True)
    email = Column(String(255),index=True)
    password = Column(String(255),index=True)

    todos = relationship("TodoTable", back_populates="parent",viewonly=True)

class TodoTable(DB_Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey("parent.id",ondelete='SET NULL'))
    create_time = Column(TIMESTAMP, index=True, default=func.now())
    title = Column(String(255),index=True)
    content = Column(String(255),index=True)

    parent = relationship("ParentTable", back_populates="todos",viewonly=True)

def create_tables():
    DB_Base.metadata.create_all(bind=SessionLocal().get_bind())
create_tables()