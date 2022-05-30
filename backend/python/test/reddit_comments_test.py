import unittest
from reddit.reddit_comments import RedditComments
import jsonschema
from utils.DBManager import DBManager


class RedditCommentsTest(unittest.TestCase):
    def __init__(self, super_method: str = "") -> None:
        self.db = DBManager("backend/config/database.json")
        super(RedditCommentsTest, self).__init__(super_method)

    def setUp(self) -> None:
        self.reddit = RedditComments(self.db)

    def tearDown(self) -> None:
        pass

    def test_json_file(self) -> None:
        NULLABLE_NUMBER = {
            "type": ["number", "string"],
            "pattern": r"^(\d+)|(null|NULL)$",
        }
        NULLABLE_STRING = {"type": ["string", "null"]}

        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "subreddit": {"type": "string"},
                "selftext": NULLABLE_STRING,
                "score": NULLABLE_NUMBER,
                "award_score": NULLABLE_NUMBER,
                "views": NULLABLE_NUMBER,
                "created_utc": {"type": "string", "format": "date-time"},
            },
        }
        mock_subreddits = [
            "cancerbiology",
        ]

        errors = []
        for subreddit in mock_subreddits:
            for response in self.reddit.request(subreddit):  # type: ignore
                try:
                    jsonschema.validate(response, schema)
                except jsonschema.exceptions.ValidationError as err:  # type: ignore
                    errors.append(err)

        self.assertEqual(errors, [], f"{errors} fields are invalid (wrong types)")
