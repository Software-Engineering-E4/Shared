import unittest
from reddit.reddit_comments import RedditComments
from utils.DBManager import DBManager


class RedditCommentsTest(unittest.TestCase):
    def __init__(self, super_method: str = "") -> None:
        self.db = DBManager("backend/config/database.json")
        super(RedditCommentsTest, self).__init__(super_method)
