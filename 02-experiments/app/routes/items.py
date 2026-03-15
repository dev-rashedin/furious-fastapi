from fastapi import APIRouter
from app.data.items import items

itemsRouter = APIRouter(prefix="/api/v1/items", tags=["items"]) 


@itemsRouter.get("/all-items")
def get_items():
  return items

@itemsRouter.post("/")
def create_item(item: dict):
  items.append(item)
  return item