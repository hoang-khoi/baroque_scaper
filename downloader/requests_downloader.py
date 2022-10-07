import pathlib
from pathlib import Path

import requests

from downloader import Downloader
from entity.album import Album
from entity.track import Track


class RequestDownloader(Downloader):
    CHUNK_SIZE = 8192

    def __download_track(self, track: Track, dir_path: [str, Path]):
        path = f'{dir_path}/{track.get_basename()}'

        with requests.get(track.url, stream=True) as req:
            with open(path, 'wb') as f:
                for chunk in req.iter_content(chunk_size=self.CHUNK_SIZE):
                    f.write(chunk)

    def download_album(self, album: Album, dir_path: [str, Path]):
        album_dir_path = pathlib.Path(f'{dir_path}/{album.name}')
        album_dir_path.mkdir(parents=True, exist_ok=True)

        print(f'Downloading album {album.name} to {album_dir_path}')

        track_count = 1
        for track in album.tracks:
            print(f'Downloading {track_count}/{len(album.tracks)}: {track.url}')
            self.__download_track(track, dir_path=album_dir_path)
            track_count += 1
