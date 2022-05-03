from datetime import datetime
from typing import Any
from reddit.reddit_requester import RedditRequester
from utils.DBManager import DBManager
import requests


class RedditComments(RedditRequester):
    def __init__(self, db: DBManager) -> None:
        super(RedditComments, self).__init__(db)
        self.db.set_table_name("reddit_comments")

    def request(self, query: Any) -> list[dict[str, str | int | datetime]]:
        res = requests.get(
            f"https://oauth.reddit.com/r/comment/hot",
            headers=self.headers,
            params={"limit": "100"},
        )
        return []
