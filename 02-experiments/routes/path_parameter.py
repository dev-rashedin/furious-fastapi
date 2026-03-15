from fastapi import APIRouter
from data.items import items

router = APIRouter()

# @router.get("/items/{item_id}")
# def get_single_item(item_id: int):
#   return {"item_id": item_id}

@router.get("/items/{item_id}")
def get_single_item(item_id: int):
  return items[item_id - 1]