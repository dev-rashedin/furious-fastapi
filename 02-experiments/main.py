from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data.items import items

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


@app.get("/items/{item_id}")
def get_single_item(item_id: int):
  return items[item_id - 1]


@app.get("/", tags=["root"])
def read_root():
  return {"message": "Hello World"}