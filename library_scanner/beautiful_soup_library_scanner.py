import requests
from bs4 import BeautifulSoup

from entity.album import Album
from helper.const import HOME_URL
from library_scanner import AlbumScouter


class BeautifulSoupLibraryScanner(AlbumScouter):
    LIBRARY_PATH = 'bmlcatalogue.html'

    def fetch_albums(self) -> list[Album]:
        req = requests.get(f'{HOME_URL}/{self.LIBRARY_PATH}')
        soup = BeautifulSoup(req.content, 'html.parser')

        albums = []

        title = soup.find('title').get_text()
        for a_tag in soup.findAll('a'):
            path = a_tag.get('href')
            if path.endswith('Web.html'):
                full_url = HOME_URL + path
                albums.append(Album(name=title, url=full_url, tracks=[]))

        return albums
