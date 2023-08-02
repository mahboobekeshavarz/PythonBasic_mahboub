from fastapi import FastAPI
from typing import Union
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my-first-api")
def hello(name:str):
    return {'Hello ' + name + '!'}

@app.get("/my-first-api")
def hello(name = None):
    if name is None:
        text = 'Hello'
    else:
        text = 'Hello ' + name + '!'
    return text


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

print(read_item(1, 'm'))