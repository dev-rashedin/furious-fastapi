from fastapi import FastAPI
from app.rotues.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
  title="Issue Tracker",
  description="Issue Tracker API",
  version="0.0.1",
  docs_url="/docs",
  redoc_url="/redoc"
)

app.middleware("http")(timing_middleware)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def root():
  return {"message": "Hello! This is the Issue Tracker API"}

@app.get("/health")
async def root():
  return {"status": "ok"}


app.include_router(issues_router)