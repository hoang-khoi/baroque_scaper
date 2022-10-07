from abc import ABC, abstractmethod

from entity.album import Album


class AlbumScouter(ABC):
    @abstractmethod
    def fetch_albums(self) -> list[Album]:
        pass
