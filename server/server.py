from typing import Union
from utils.db_api.sqlite import db
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    admins = db.select_all_admins()
    print(admins)
    return {"admins": admins}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

async def run_fastapi():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()