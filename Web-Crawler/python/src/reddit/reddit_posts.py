from dataclasses import dataclass
from datetime import datetime
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

        keys_not_found: set[str] = {""}
        out: list[dict[str, str | int | datetime]] = []
        for post in res.json()["data"]["children"]:
            data: dict[str, str | int | datetime] = {}

            for column in self.columns:
                if column == "created_utc":
                    data[column] = str(datetime.fromtimestamp(post["data"][column]))[
                        :10
                    ]
                else:
                    try:
                        data[column] = post["data"][column]
                    except KeyError:
                        keys_not_found.add(column)
                        data[column] = "NULL"
            out.append(data)

        return out
