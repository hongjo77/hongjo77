# from fastapi import APIRouter, FastAPI, HTTPException
# from typing import List, Optional

# from schema import *
# from service.todo import TodoService
# from service.item import ItemService

# router = APIRouter(
#     prefix="/item",
#     tags=["item"],
#     responses={404: {"description": "Not found"}},
# )

# itemService = ItemService()

# @router.post("/user")
# async def root(name: str):
#     itemService.createUser(name)
#     return {"message": "ok"}

# @router.get("/user/{user_id}")
# async def root(user_id: int):
#     user = itemService.getUserById(user_id)

#     if user is None:
#         raise HTTPException(status_code=404, detail="user not found")
    
#     return {"user": user}

# @router.post("/item/{user_id}")
# async def root(user_id: int,name: str):
#     itemService.createItem(user_id,name)
#     return {"message": "ok"}



# @router.get("/items")
# async def root():
#     item = itemService.getAllItem()
    
#     return {"item": item} if item else {"item": None}


# @router.get("/user/{user_id}/items")
# async def root(user_id: int):
#     item = itemService.getAllItemOfUser(user_id)
    
#     return {"item": item} if item else {"item": None}

# @router.get("/user/{user_id}/{id}/items")
# async def root(user_id: int, id: int):
#     item = itemService.getOneItemOfUser(user_id,id)
    
#     return {"item": item} if item else {"item": None}

# @router.put("/item/{user_id}/{id}")
# async def root(user_id: int, id: int,name: str) -> bool:
#     itemService.putItem(user_id,id,name)


# @router.delete("/item/{user_id}/{id}")
# async def root(user_id: int, id: int) -> bool:
#     itemService.delItem(user_id,id)