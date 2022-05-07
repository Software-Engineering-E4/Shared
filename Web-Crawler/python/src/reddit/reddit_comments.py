from dataclasses import dataclass
from datetime import datetime
from typing import Any
from reddit.reddit_requester import RedditRequester
import requests


@dataclass
class RedditComments(RedditRequester):
    def __post_init__(self) -> None:
        self.db.set_table_name("reddit_comments")

    def request(self, query: Any) -> list[dict[str, str | int | datetime]]:
        res = requests.get(
            f"https://oauth.reddit.com/r/comment/hot",
            headers=self.headers,
            params={"limit": "100"},
        )
        return []

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        return ""
