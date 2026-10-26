from fastapi import FastAPI, HTTPException, status

import models
from database import DEFAULT_ERROR_INT, Anime, IMDatabase

app = FastAPI()

database = IMDatabase()
database.seed()


@app.get("/anime")
async def anime_get_all():
    return database.anime_get_all()


@app.get("/anime/{id}")
async def anime_get_one(id: int):
    anime = database.anime_get_by_id(id)

    if not anime:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "anime does not exists",
        )

    return anime


@app.post("/anime", status_code=status.HTTP_201_CREATED)
async def anime_create(anime: models.AnimeCreate):
    anime_id = database.anime_create(
        Anime(
            title=anime.title,
            year=anime.year,
            episode_count=anime.episode_count,
        )
    )

    if anime_id == DEFAULT_ERROR_INT:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="anime already exists",
        )

    return {"id": anime_id}


@app.delete("/anime/{id}")
async def anime_delete(id: int, status_code=status.HTTP_204_NO_CONTENT):
    database.anime_delete_by_id(id)


@app.patch("/anime/{id}")
async def anime_update(id: int, anime_in: models.AnimeUpdate):
    update_data = anime_in.model_dump(exclude_unset=True)

    if not update_data:
        existing = database.anime_get_by_id(id)
        if not existing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="anime not found",
            )
        return existing

    updated_anime = database.anime_update(id, update_data)

    if not updated_anime:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="anime not found",
        )

    return updated_anime
