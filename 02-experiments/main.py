from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.items import itemsRouter
from app.routes.path_parameter import pathParameterRouter
from app.routes.query_parameter import queryParameterRouter

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


# Health check
@app.get("/health")
def health_check():
  return {"status": "ok"}



# Add router
app.include_router(itemsRouter)
app.include_router(pathParameterRouter)
app.include_router(queryParameterRouter)


# Root
@app.get("/", tags=["root"])
def read_root():
  return {"message": "Hello World"}