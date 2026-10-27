from pydantic import BaseModel
from sqlmodel import SQLModel

class AnimeCreate(BaseModel):
    title: str
    year: int
    episode_count: int


class AnimeUpdate(BaseModel):
    title: str | None = None
    year: int | None = None
    episode_count: int | None = None
