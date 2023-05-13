import pathlib
import shutil
from unittest import TestCase

from downloader.requests_downloader import RequestDownloader
from entity.album import Album
from entity.track import Track


class TestRequestTrackDownloader(TestCase):

    def setUp(self) -> None:
        self.ALBUM_NAME = 'SampleAlbum'

        self.track = Track(url='https://www.baroquemusic.org/DLower/501BarocophileTr1AlbinoniSinfonia.mp3', name='')
        self.track2 = Track(url='https://www.baroquemusic.org/DLower/504BachophileTr1Cantata76.mp3', name='')
        self.album = Album(name=self.ALBUM_NAME, url='', tracks=[self.track, self.track2])
        self.under_test = RequestDownloader()

    def tearDown(self) -> None:
        album_path = self.__album_path()
        shutil.rmtree(album_path)

    def test_download_album(self):
        self.under_test.download_album(self.album, dir_path=pathlib.Path().absolute())

    def test_download_album_folder_existed_skip(self):
        self.__album_path().mkdir()
        self.under_test.download_album(self.album, dir_path=pathlib.Path().absolute())

    def __album_path(self) -> pathlib.Path:
        return pathlib.Path(self.ALBUM_NAME)
