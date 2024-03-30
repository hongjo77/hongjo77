from fastapi import APIRouter, FastAPI, HTTPException,Header, Depends
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder

from schema import *
from schema.parent import *

from service.parent import ParentService
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer


router = APIRouter(
    prefix="/parent",
    tags=["parent"],
    responses={404: {"description": "Not found"}},
)

parentService = ParentService()

@router.post("/parent")
async def root(data: CreateParentInput):
    parent = parentService.createParent(data)

    return JSONResponse(status_code=201, content={
        'parent': jsonable_encoder(parent),
        'x-jwt': signJWT(parent.id)
    })


@router.get("/parent/id/{input}")
async def root(input : int):
    id=GetParentByIdInput(id=input)
    parent = parentService.getParentById(id)

    if parent is None:
        raise HTTPException(status_code=404, detail="parent not found")
    
    return parent


@router.get("/parent/email/{input}")
async def root(input: str):
    email=GetParentByEmailInput(email=input)
    parent = parentService.getParentByEmail(email)

    if parent is None:
        raise HTTPException(status_code=404, detail="parent not found")
    
    return parent


@router.put("/parent/update")
async def root(input: UpdateParentInput, uid: str = Depends(JWTBearer())):
    parentService.updateParent(input)


@router.delete("/parent/delete")
async def root(input: DeleteParentInput):
    parentService.deleteParent(input)






