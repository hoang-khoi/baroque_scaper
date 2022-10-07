import pathlib
from unittest import TestCase

from downloader.requests_downloader import RequestDownloader
from entity.album import Album
from entity.track import Track


class TestRequestTrackDownloader(TestCase):
    def setUp(self) -> None:
        self.track = Track(url='http://www.baroquemusic.org/DLower/501BarocophileTr1AlbinoniSinfonia.mp3', name='')
        self.album = Album(name='Sample Name', url='', tracks=[self.track])
        self.under_test = RequestDownloader()

    def test_download_track(self):
        self.under_test.__download_track(self.track, pathlib.Path().absolute())

    def test_download_album(self):
        self.under_test.download_album(self.album, dir_path=pathlib.Path().absolute())
