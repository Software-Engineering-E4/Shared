import unittest
from utils.DBManager import DBManager


class YoutubeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = DBManager("Web-Crawler/python/config/database.json")

    def tearDown(self) -> None:
        self.db.__exit__()

    def test_db_connection(self) -> None:
        pass
