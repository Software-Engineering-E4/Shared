import unittest
from youtube.youtube_comments import YoutubeComments
from utils.DBManager import DBManager


class YoutubeCommentsTest(unittest.TestCase):
    def __init__(self, super_method: str = "") -> None:
        self.db = DBManager("backend/config/database.json")
        super(YoutubeCommentsTest, self).__init__(super_method)
