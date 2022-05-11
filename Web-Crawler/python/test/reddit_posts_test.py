import unittest
import jsonschema
import requests
from src.reddit.reddit_posts import RedditPosts
from utils.DBManager import DBManager


class RedditPostsTest(unittest.TestCase):
    def __init__(self, super_method: str = "") -> None:
        self.db = DBManager("Web-Crawler/python/config/database.json")
        super(RedditPostsTest, self).__init__(super_method)

    def setUp(self) -> None:
        self.reddit = RedditPosts(self.db)

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
            "cancerfamilysupport",
            "cancercaregivers",
            "colorectalcancer",
        ]

        errors = []
        for subreddit in mock_subreddits:
            for f in self.reddit.request(subreddit):
                try:
                    jsonschema.validate(f, schema)
                except jsonschema.exceptions.ValidationError as err:  # type: ignore
                    errors.append(err)

        self.assertEqual(errors, [], f"{errors} fields are invalid (wrong types)")

    def test_initial_response(self) -> None:
        res = requests.get(
            f"https://oauth.reddit.com/r/cancer/hot",
            headers=self.reddit.headers,
            params={"limit": "100"},
        )
        self.assertTrue(res.ok, f"Response status is {res.status_code}")

    def test_bad_request(self) -> None:
        self.assertRaises(
            Exception,
            requests.get,
            f"https://oauth.reddit.com/wrong_call",
            headers=self.reddit.headers,
            params={"limit": "100"},
            msg="Expected 400 - bad request",
        )

    def test_forbidden_request(self) -> None:
        self.reddit.headers["Authorization"] = ""
        res = requests.get(
            f"https://oauth.reddit.com/r/cancer/hot",
            headers=self.reddit.headers,
            params={"limit": "100"},
        )
        self.assertTrue(res.status_code == 403, "Status code should be 403")
