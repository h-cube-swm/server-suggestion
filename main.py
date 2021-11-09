import uvicorn
import json
from fastapi import FastAPI
from tester import get_order
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()


class Item(BaseModel):
    text: str


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Result": "Server Alive."}


@app.get("/test")
async def order(text: str):
    text = text.strip()
    if(len(text) > 2):
        _order = get_order(text)
    else:
        _order = []
    return JSONResponse(_order)
