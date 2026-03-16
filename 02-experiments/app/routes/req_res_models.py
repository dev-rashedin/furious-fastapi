from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

reqResModelsRouter = APIRouter(prefix="/api/v1/items", tags=["items"])

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@reqResModelsRouter.post("/items/")
async def create_item(item: Item):
    return item