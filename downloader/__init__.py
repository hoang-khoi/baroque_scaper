from abc import ABC, abstractmethod
from pathlib import Path

from entity.album import Album
from entity.track import Track


class Downloader(ABC):
    @abstractmethod
    def download_album(self, album: Album, dir_path: [str, Path]):
        pass
