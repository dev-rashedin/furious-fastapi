import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOut, IssueUpdate
from app.storage import load_data, save_data


router = APIRouter(prefix="/api/v1/issues", tags=["issues"])



# Get all the issues
@router.get("/", response_model=list[IssueOut])
async def get_issues():
  """ Get all the issues """
  issues = load_data()
  return issues

# Create a new issue
@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
async def create_issue():
  """ Create a new issue """
  issues = load_data()
  new_issue = {
    "id": str(uuid.uuid4()),
    "title": "New issue",
    "description": "New issue description",
    "priority": "low",
    "status": "open"
  }
  return {"id": str(uuid.uuid4())}