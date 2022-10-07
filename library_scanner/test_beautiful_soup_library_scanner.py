from unittest import TestCase

from library_scanner.beautiful_soup_library_scanner import BeautifulSoupLibraryScanner


class TestBeautifulSoupLibraryScanner(TestCase):
    def setUp(self) -> None:
        self.under_test = BeautifulSoupLibraryScanner()

    def test_fetch_albums(self):
        albums = self.under_test.fetch_albums()
        print(albums)
