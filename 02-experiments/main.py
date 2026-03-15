from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data.items import items
from routes.path_parameter import router

# Create app with metadata
app = FastAPI(
    title="Furious FastAPI",
    version="0.0.1",
    description="A complete guide to FastAPI",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "Furious FastAPI",
        "url": "https://fastapi.tiangolo.com/",
    },
)

# Add CORS middleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.get("/health")
def health_check():
  return {"status": "ok"}


@app.get("/items")
def get_items():
  return items


# Add router
app.include_router(router)


@app.get("/", tags=["root"])
def read_root():
  return {"message": "Hello World"}