from fastapi import APIRouter, Query
from typing import Optional, List

queryParameterRouter = APIRouter()

@queryParameterRouter.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
  return {"skip": skip, "limit": limit}


@queryParameterRouter.get("/search/")
async def search(q: Optional[str] = None):
  return {"query": q}


# Query parameters with validation
@queryParameterRouter.get("/items/search/")
async def search_items(
    q: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        title="Search query"
    ),
    price_min: float = Query(0, ge=0),
    price_max: Optional[float] = Query(None, le=10000),
    tags: List[str] = Query(default=[])
):
    results = {"items": []}
    if q:
        results["q"] = q
    results["price_range"] = [price_min, price_max]
    results["tags"] = tags
    return results