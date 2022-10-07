from abc import ABC, abstractmethod

from entity.album import Album


class AlbumScanner(ABC):
    @abstractmethod
    def scan_and_fill(self, album: Album) -> Album:
        pass
