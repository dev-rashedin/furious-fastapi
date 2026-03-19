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


# Get a single issue
@router.get("/{issue_id}", response_model=IssueOut)
async def get_single_issue(issue_id: str):
  """ Get a single issue """
  issues = load_data()

  for issue in issues:
    if issue["id"] == issue_id:
      return issue
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


# Create a new issue
@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
async def create_issue(payload: IssueCreate):

  """ Create a new issue """
  issues = load_data()
  new_issue = {
    "id": str(uuid.uuid4()),
    "title": payload.title,
    "description": payload.description,
    "priority": payload.priority,
    "status": "open"
  }

  issues.append(new_issue)
  save_data(issues)

  return new_issue


# Update a issue
@router.put("/{issue_id}", response_model=IssueOut)
async def update_issue(issue_id: str, payload: IssueUpdate):

  """ Update a issue """
  issues = load_data()

  for issue in issues:
    if issue["id"] == issue_id:
      if payload.title is not None:
        issue["title"] = payload.title
      if payload.description is not None:
        issue["description"] = payload.description
      if payload.priority is not None:
        issue["priority"] = payload.priority
      if payload.status is not None:
        issue["status"] = payload.status

      save_data(issues)
      return issue

  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


# Delete a issue
@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_issue(issue_id: str):
  """ Delete n issue by id"""
  issues = load_data()

  for i, issue in enumerate(issues):
    if issue["id"] == issue_id:
      issues.pop(i)
      save_data(issues)
      return

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Issue not found"
    )