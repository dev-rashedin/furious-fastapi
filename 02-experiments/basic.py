from fastapi import FastAPI

app = FastAPI()


items = [
  {"id": 1, "name": "Item One"},
  {"id": 2, "name": "Item Two"},
  {"id": 3, "name": "Item Three"}
]

@app.get("/health")
def health_check():
  return {"status": "ok"}


@app.get("/items")
def get_items():
  return items


@app.get("/items/{item_id}")
def get_single_item(item_id: int):
  return items[item_id - 1]