from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()

@router.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
  return {"skip": skip, "limit": limit}


@router.get("/search/")
async def search(q: Optional[str] = None):
  return {"query": q}