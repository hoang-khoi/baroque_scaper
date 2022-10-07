import os
from dataclasses import dataclass

import requests


@dataclass
class Track:
    name: [str, None]
    url: str

    def get_basename(self) -> str:
        return os.path.basename(self.url)
