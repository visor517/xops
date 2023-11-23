from fastapi import APIRouter, Query
from time import time
import uuid

from models import VisitedLinksIn, VisitedLinksOut
from db.base import database
from db.tables import visited_links


router = APIRouter()


@router.get("/", response_model=VisitedLinksOut, 
            description="Получить список доменов посещенных работником",)
async def read_visited_links(
    from_: int = Query(
        None,
        description="С какого времени в формате (число секунд с начала эпохи)",
        alias="from",
    ),
    to: int = Query(None, description="По какое время в формате (число секунд с начала эпохи)"),
):
    query = visited_links.select().distinct(visited_links.c.domain)
    if from_:
        query = query.where(visited_links.c.visited_at >= from_)
    if to:
        query = query.where(visited_links.c.visited_at <= to)
    res = await database.fetch_all(query)
    domains = [item["domain"] for item in res]
    return {"domains": domains}


@router.post("/", status_code=200,
             description="Отправить список ссылок, которые были посещены работником",)
async def create_visited_links(data: VisitedLinksIn):
    request_time = round(time())
    for link in data.links:
        uid = str(uuid.uuid1())
        query = visited_links.insert().values(id=uid, domain=link.host, visited_at=request_time)
        await database.execute(query)
    return {"status": "ok"}
