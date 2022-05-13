import unittest
from utils.DBManager import DBManager
from youtube.youtube_videos import YoutubeVideos


class YoutubeVideosTest(unittest.TestCase):
    def __init__(self, super_method: str = "") -> None:
        super().__init__(super_method)
        self.db = DBManager("backend/python/config/database.json")

    def setUp(self) -> None:
        self.youtube = YoutubeVideos(self.db)

    def tearDown(self) -> None:
        pass
