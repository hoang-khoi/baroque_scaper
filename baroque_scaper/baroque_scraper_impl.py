from pathlib import Path

from album_scanner.beautiful_soup_album_scanner import BeautifulSoupAlbumScanner
from baroque_scaper import BaroqueScaper
from downloader.requests_downloader import RequestDownloader
from library_scanner.beautiful_soup_library_scanner import BeautifulSoupLibraryScanner


class BaroqueScaperImpl(BaroqueScaper):
    def __init__(
            self,
            library_scanner=BeautifulSoupLibraryScanner(),
            album_scanner=BeautifulSoupAlbumScanner(),
            downloader=RequestDownloader(),
    ):
        self.library_scanner = library_scanner
        self.album_scanner = album_scanner
        self.downloader = downloader

    def scrape(self, dir_path: [str, Path]):
        albums = self.library_scanner.fetch_albums()

        album_count = 1
        for album in albums:
            self.album_scanner.scan_and_fill(album)
            print(f'Downloading album {album_count}/{len(albums)} {album.name} to {dir_path}')
            self.downloader.download_album(album, dir_path)
            album_count += 1
