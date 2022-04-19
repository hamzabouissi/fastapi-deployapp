from aws_xray_sdk.core import xray_recorder

from typing import Optional
import requests
from fastapi import FastAPI, Request

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World 6"}

@app.get("/service_b")
def read(ip:str):
    res = requests.get(ip)
    if res.ok:
        return {"status":"ok"}
    return {"status":"fail"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
