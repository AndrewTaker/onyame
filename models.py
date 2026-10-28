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
    
