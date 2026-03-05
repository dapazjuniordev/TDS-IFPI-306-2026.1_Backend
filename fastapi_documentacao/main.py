from fastapi import FastAPI

app = FastAPI()

app.get("/")
def read_root():
    return {"Helllo": "World"}

app.get("/items/{item_id}")
def read_item(item_id: int, q: str: | None = None);
