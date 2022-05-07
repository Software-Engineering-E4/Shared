from dataclasses import dataclass
from datetime import datetime
from typing import Any
import requests
from reddit.reddit_requester import RedditRequester
from utils.DBManager import DBManager


@dataclass
class RedditPosts(RedditRequester):
    db: DBManager

    def __post_init__(self) -> None:
        super().__post_init__()
        self.set_table_name("reddit_posts")

    def request(self, subreddit: str) -> list[dict[str, str | int | datetime]]:
        res = requests.get(
            f"https://oauth.reddit.com/r/{subreddit}/hot",
            headers=self.headers,
            params={"limit": "100"},
        )

        out: list[dict[str, str | int | datetime]] = []
        for post in res.json()["data"]["children"]:
            data: dict[str, str | int | datetime] = {}

            for column in self.columns:
                data[column] = self.treat_special_case(column, post)
                if data[column]:
                    continue
                try:
                    data[column] = post["data"][column]
                except KeyError:
                    data[column] = "NULL"
            out.append(data)

        return out

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        match column:
            case "created_utc":
                return str(datetime.fromtimestamp(item["data"][column]))[:10]
            case _:
                return ""
