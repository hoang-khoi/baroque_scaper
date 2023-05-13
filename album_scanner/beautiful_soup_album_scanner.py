import requests
from bs4 import BeautifulSoup

from album_scanner import AlbumScanner
from entity.album import Album
from entity.track import Track
from helper.const import HOME_URL


class BeautifulSoupAlbumScanner(AlbumScanner):
    def scan_and_fill(self, album: Album) -> Album:
        assert album.url
        assert album.tracks == []

        req = requests.get(album.url)
        soup = BeautifulSoup(req.content, 'html.parser')

        album.name = soup.find('title').get_text()

        for a_tag in soup.findAll('a'):
            path = a_tag.get('href')
            print(f'Path: {path}')
            if path.endswith('.mp3'):
                full_url = HOME_URL + path
                album.tracks.append(Track(name=path, url=full_url))

        return album
