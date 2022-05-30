import unittest
from youtube.youtube_comments import YoutubeComments
from utils.DBManager import DBManager
import jsonschema


class YoutubeCommentsTest(unittest.TestCase):
    def __init__(self, super_method: str = "") -> None:
        self.db = DBManager("backend/config/database.json")
        super(YoutubeCommentsTest, self).__init__(super_method)

    def setUp(self) -> None:
        self.youtube = YoutubeComments(self.db)

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
                "title": {"type": "string"},
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
            for response in self.youtube.request(subreddit): # type: ignore
                try:
                    jsonschema.validate(response, schema)
                except jsonschema.exceptions.ValidationError as err:  # type: ignore
                    errors.append(err)

        self.assertEqual(errors, [], f"{errors} fields are invalid (wrong types)")
