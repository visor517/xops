from fastapi import FastAPI

from handlers import visited_links


app = FastAPI(title="XOps")


app.include_router(visited_links.router, prefix="/visited_links", tags=["visited_links"])
