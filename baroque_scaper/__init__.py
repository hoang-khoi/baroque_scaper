from abc import ABC, abstractmethod
from pathlib import Path


class BaroqueScaper(ABC):
    @abstractmethod
    def scap(self, dir_path: [str, Path]):
        pass
