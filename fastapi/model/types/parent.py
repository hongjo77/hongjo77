from pydantic import BaseModel


class Parent(BaseModel):
    id : int
    name : str
    email : str
    password : str
    #todo : str
    
    class Config:
        orm_mode = True