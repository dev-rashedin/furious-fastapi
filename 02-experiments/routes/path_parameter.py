from fastapi import APIRouter, Path
from data.items import items
from enum import Enum

router = APIRouter()

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"


# Path parameters with validation
@router.get("/items/{item_id}")
def get_single_item(item_id: int = Path(
  title="The ID of the item to get",
  description="The ID of the item to get",
  gt=0,
  le=100
)):
  return items[item_id - 1]

# Enum path parameter
@router.get("/models/${model_name}")
async def get_model(model_name: ModelName):
  if model_name == ModelName.alexnet:
    return {"model_name": model_name, "message": "Deep Learning FTW!"}

  if model_name.value == "lenet":
    return {"model_name": model_name, "message": "LeCNN all the images"}

  return {"model_name": model_name, "message": "Have some residuals"}