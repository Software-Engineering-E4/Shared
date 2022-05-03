import unittest
from src.youtube_comments import YoutubeComments
from utils.DBManager import DBManager


class YoutubeCommentsTest(unittest.TestCase):
    def __init__(self, super_method: str = "") -> None:
        self.db = DBManager("Web-Crawler/python/config/database.json")
        super(YoutubeCommentsTest, self).__init__(super_method)
