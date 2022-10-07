from dataclasses import dataclass

from entity.track import Track


@dataclass
class Album:
    name: [str, None]
    url: str
    tracks: list[Track]
