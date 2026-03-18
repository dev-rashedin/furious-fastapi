from fastapi import FastAPI
from app.rotues.issues import router as issues_router


app = FastAPI(
  title="Issue Tracker",
  description="Issue Tracker API",
  version="0.0.1",
  docs_url="/docs",
  redoc_url="/redoc"
)

@app.get("/")
def root():
  return {"message": "Hello! This is the Issue Tracker API"}

@app.get("/health")
async def root():
  return {"status": "ok"}


app.include_router(issues_router)