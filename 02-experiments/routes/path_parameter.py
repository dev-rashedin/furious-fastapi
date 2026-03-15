from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
def get_single_item(item_id: int):
  return {"item_id": item_id}