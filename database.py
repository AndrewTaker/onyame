from typing import Literal

from pydantic import BaseModel

DEFAULT_ERROR_INT: int = -1


class Anime(BaseModel):
    id: int | None = None
    title: str
    year: int
    episode_count: int


class Manga(BaseModel):
    id: int | None = None
    title: str
    year: int
    chapter_count: int


INITIAL_ANIME = [
    Anime(id=1, title="Naruto", year=2002, episode_count=220),
    Anime(id=2, title="Bleach", year=2004, episode_count=366),
    Anime(id=3, title="Death Note", year=2006, episode_count=37),
    Anime(id=4, title="Fullmetal Alchemist: Brotherhood", year=2009, episode_count=64),
    Anime(id=5, title="Attack on Titan", year=2013, episode_count=89),
    Anime(id=6, title="One Piece", year=1999, episode_count=1088),
    Anime(id=7, title="Demon Slayer", year=2019, episode_count=55),
    Anime(id=8, title="Jujutsu Kaisen", year=2020, episode_count=47),
    Anime(id=9, title="Hunter x Hunter", year=2011, episode_count=148),
    Anime(id=10, title="Steins;Gate", year=2011, episode_count=24),
    Anime(id=11, title="Cowboy Bebop", year=1998, episode_count=26),
    Anime(id=12, title="Cyberpunk: Edgerunners", year=2022, episode_count=10),
]


class IMDatabase:
    def __init__(self) -> None:
        self.__anime: dict[int, Anime] = {}
        self.__manga: dict[int, Manga] = {}

    # anime block
    def anime_get_all(self) -> list[Anime]:
        entries: list[Anime] = []

        for id, anime in self.__anime.items():
            entries.append(
                Anime(
                    id=id,
                    title=anime.title,
                    year=anime.year,
                    episode_count=anime.episode_count,
                )
            )

        return entries

    def anime_get_by_id(self, target_id: int) -> Anime | None:
        for id, anime in self.__anime.items():
            if id == target_id:
                return anime
        return None

    def anime_get_by_title(self, target_title: str) -> Anime | None:
        for id, anime in self.__anime.items():
            if anime.title == target_title:
                return anime
        return None

    def anime_create(self, anime: Anime) -> int:
        anime.id = self.__autoincrement("anime")
        titles = [a.title for a in self.__anime.values()]

        if anime.title in titles:
            return DEFAULT_ERROR_INT

        self.__anime[anime.id] = anime

        return anime.id

    def anime_delete_by_id(self, id: int) -> None:
        del self.__anime[id]

    def anime_update(self, id: int, update_data: dict) -> Anime | None:
        if id not in self.__anime:
            return None

        anime = self.__anime[id]

        for key, value in update_data.items():
            setattr(anime, key, value)

        return anime

    def seed(self) -> None:
        for a in INITIAL_ANIME:
            self.anime_create(a)

    # extra private methods
    def __autoincrement(self, model: Literal["anime", "manga"]) -> int:
        if model == "anime":
            ids = [id for id in self.__anime.keys()]
        elif model == "manga":
            ids = [id for id in self.__manga.keys()]

        if not ids:
            return 1

        current_max_id = max(ids)
        return current_max_id + 1
