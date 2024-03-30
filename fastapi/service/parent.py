from fastapi import APIRouter, FastAPI

from model.parent import ParentTable
from model.todo import TodoTable

from schema import *
from schema.parent import *

from db import get_db_session


class ParentService:

    def createParent(self, p: CreateParentInput) -> CreateParentOutput:
        db=get_db_session()
        try:
            parent = ParentTable(name=p.name, email=p.email,password=p.password)
            db.add(parent)
            db.commit()
            db.refresh(parent)

            return parent
        except Exception as e:
            db.rollback()
            raise Exception(e)
        
    def getParentById(self, p: GetParentByIdInput) -> GetParentByIdOutput:
        db=get_db_session()
        try:
            parent = db.query(ParentTable).filter(ParentTable.id==p.id).first()
        
            return parent
        except Exception as e:
            raise Exception(e)
        
    def getParentByEmail(self, p: GetParentByEmailInput) -> GetParentByEmailOutput:
        db=get_db_session()
        try:
            parent = db.query(ParentTable).filter(ParentTable.email==p.email).first()
            
            return parent
        except Exception as e:
            #raise HTTPException(status_code=500, detail="Internal server error")
            raise Exception(e)


    def updateParent(self, p: UpdateParentInput) -> bool:
        db=get_db_session()
        try:
            parent = db.query(ParentTable).filter(ParentTable.id==p.parent.id).first()
            if parent is None:
                return False
            
            setattr(parent, "name", p.parent.name)
            setattr(parent, "email", p.parent.email)
            setattr(parent, "password", p.parent.password)
                
            db.commit()

            return True
        except Exception as e:
            db.rollback()
            raise Exception(e)

    def deleteParent(self, p: DeleteParentInput)-> bool:
        db=get_db_session()
        try:
            parent = db.query(ParentTable).filter(ParentTable.id==p.id).first()
            if parent is None:
                return False
            
            db.delete(parent)
            db.commit()

            return True
        except Exception as e:
            db.rollback()
            raise Exception(e)
