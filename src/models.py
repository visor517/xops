from pydantic import BaseModel, AnyUrl


class VisitedLinksIn(BaseModel):
    links: list[AnyUrl]


class VisitedLink(BaseModel):
    id: str
    domain: str
    visited_at: int


class VisitedLinksOut(BaseModel):
    domains: list[str]
    status: str = "ok"
