from dataclasses import dataclass
from datetime import datetime
import logging
from typing import Any
import requests
from reddit.reddit_requester import RedditRequester


@dataclass
class RedditPosts(RedditRequester):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.logger = logging.getLogger(__name__)
        self.set_table_name("reddit_posts")

    def request(self, subreddit: str) -> list[dict[str, str | int]]:
        res = requests.get(
            f"{self.link}/{subreddit}/hot",
            headers=self.headers,
            params={"limit": "100"},
        )

        out: list[dict[str, str | int]] = []
        for post in res.json()["data"]["children"]:
            data: dict[str, str | int] = {}

            for column in self.columns:
                data[column] = self.treat_special_case(column, post)
                if data[column] != "":
                    continue
                try:
                    data[column] = post["data"][column]
                except KeyError:
                    data[column] = "NULL"
            if self.real_time:
                self.send_to_db([data], self.columns)
            else:
                out.append(data)

        return out

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        match column:
            case "created_utc":
                return str(datetime.fromtimestamp(item["data"][column]))[:10]
            case "link":
                return f"https://www.reddit.com/{item['data']['id']}"
            case _:
                return ""

    def request_has_error(self, result: requests.Response) -> bool:
        return super().request_has_error(result)
