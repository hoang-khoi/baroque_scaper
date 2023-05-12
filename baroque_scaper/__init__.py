from abc import ABC, abstractmethod
from pathlib import Path


class BaroqueScaper(ABC):
    @abstractmethod
    def scrape(self, dir_path: [str, Path]):
        pass
