from pydantic import BaseModel


class Todo(BaseModel):
    id : int
    parent_id : int
    create_time : str
    title : str
    content : str
    
    class Config:
        orm_mode = True