import unittest
from utils.DBManager import DBManager
from src.youtube import Youtube


class YoutubeTest(unittest.TestCase):
    def __init__(self, super_method: str = "") -> None:
        super().__init__(super_method)
        self.db = DBManager("Web-Crawler/python/config/database.json")

    def setUp(self) -> None:
        self.youtube = Youtube(self.db)

    def tearDown(self) -> None:
        pass
