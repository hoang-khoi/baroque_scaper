from unittest import TestCase

from album_scanner.beautiful_soup_album_scanner import BeautifulSoupAlbumScanner
from entity.album import Album


class TestBeautifulSoupAlbumScanner(TestCase):
    def setUp(self) -> None:
        self.under_test = BeautifulSoupAlbumScanner()

    def test_scan_and_fill(self):
        album = self.under_test.scan_and_fill(album=Album(
            name=None,
            url='http://www.baroquemusic.org/5012Web.html',
            tracks=[]
        ))

        self.assertEqual('The Barocophile - A Double Album Special for Baroque-Music-Lovers', album.name)
        self.assertTrue(len(album.tracks) > 0)
