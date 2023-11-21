from fastapi import FastAPI

from db.base import database
from handlers import visited_links


app = FastAPI(title="XOps")

app.include_router(visited_links.router, prefix="/visited_links", tags=["visited_links"])


@app.get("/")
async def root():
    return {"message": "XOps running!!!"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
