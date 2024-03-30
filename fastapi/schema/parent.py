from pydantic import BaseModel
from typing import List, Optional
from model.types.parent import Parent

class CreateParentInput(BaseModel):
    name : str
    email : str
    password : str

class CreateParentOutput(BaseModel):
    parent : Parent

class GetParentByIdInput(BaseModel):
    id : int

class GetParentByIdOutput(BaseModel):
    parent : Optional[Parent]

class GetParentByEmailInput(BaseModel):
    email : str

class GetParentByEmailOutput(BaseModel):
    parent : Optional[Parent]


class UpdateParentInput(BaseModel):
    parent : Parent
    
class DeleteParentInput(BaseModel):
    id:int