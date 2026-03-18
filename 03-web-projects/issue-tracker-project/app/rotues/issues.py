import uuid
from fastapi import APIRouter, status


router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_issue():
  return {"id": str(uuid.uuid4())}