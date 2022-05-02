from distutils.log import error
import unittest
from src.reddit import Reddit
from utils.DBManager import DBManager
import jsonschema


class RedditTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = DBManager("Web-Crawler/python/config/database.json")

    def tearDown(self) -> None:
        self.db.__exit__()

    def test_json_file(self) -> None:
        reddit = Reddit(self.db)
        schema = {
            "type": "object",
            "properties": {
                "subreddit": {"type": "string"},
                "title": {"type": "string"},
                "selftext": {"type": "string"},
                "upvote_ratio": {"type": "number", "minimum": 0},
                "ups": {"type": "number", "minimum": 0},
                "downs": {"type": "number", "minimum": 0},
                "score": {"type": "number", "minimum": 0},
            },
        }
        mock_subreddits = [
            "cancerbiology",
            "cancerfamilysupport",
            "cancercaregivers",
            "colorectalcancer",
        ]

        errors = []
        for subreddit in mock_subreddits:
            try:
                for f in reddit.request(subreddit):
                    jsonschema.validate(f, schema)
            except jsonschema.exceptions.ValidationError as err:
                errors.append(err)

        self.assertTrue(len(errors) == 0, f"{len(errors)} fields are invalid")

    def test_initial_response(self) -> None:
        pass
