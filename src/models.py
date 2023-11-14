from pydantic import BaseModel, model_validator, AnyUrl
from urllib.parse import urlparse


class VisitedLinksIn(BaseModel):
    link: AnyUrl
    domain: str

    # разбиваем link
    @model_validator(mode="after")
    def separate_link(cls, values: dict) -> dict:
        if "link" in values:
            values["domain"] = urlparse(values["link"]).netloc
        return values


class VisitedLinks(VisitedLinksIn):
    id: str
    visited_at: str
