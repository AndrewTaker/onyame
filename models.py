from sqlmodel import SQLModel, Field

# студия которая сделала аниме
class Studios(SQLModel, table=True):
    id : int | None = Field(primary_key=True, default=None)
    name : str
    founded_year : int | None = Field(default=None)
    
class Creators(SQLModel, table=True):
    id : int | None = Field(primary_key=True, default=None)
    name : str
    birth_year : int | None = Field(default=None)
    
class Manga(SQLModel, table=True):
    id : int | None = Field(primary_key=True, default=None)
    title : str
    creator_id : int | None = Field(default=None)
    chapters : int | None = Field(default=None)
    status : str | None = Field(default=None)
    
class Anime(SQLModel, table=True):
    id : int | None = Field(primary_key=True, default=None)
    title : str
    studio_id : int | None = Field(default=None)
    
