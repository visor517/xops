import sqlalchemy
from time import time

from db.base import metadata


def default_time():
    return round(time())


visited_links = sqlalchemy.Table(
    "visited_links",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("domain", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("visited_at", sqlalchemy.Integer, default=default_time),
)