from fastapi import APIRouter
import uuid

from models import VisitedLinks, VisitedLinksIn
from db.base import database
from db.tables import visited_links


router = APIRouter()

@router.get('/', response_model=list[VisitedLinks])
async def read_visited_links():
    query = visited_links.select()
    return await database.fetch_all(query)


@router.post('/', status_code=200)
async def create_visited_links(data: VisitedLinksIn):
    uid = str(uuid.uuid1())
    query = visited_links.insert().values(
        id=uid,
        domain=data.domain,
    )
    await database.execute(query)
    return "ok"
