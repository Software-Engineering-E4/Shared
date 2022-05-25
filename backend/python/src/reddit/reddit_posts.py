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

    def request(self, subreddit: str) -> None:
        res = requests.get(
            f"{self.link}/{subreddit}/hot",
            headers=self.headers,
            params={"limit": "100"},
        )

        self.treat_response(res)

    def treat_response(self, res: requests.Response):
        for post in res.json()["data"]["children"]:
            db_row: dict[str, str | int] = {}

            for column in self.columns:
                db_row[column] = self.treat_special_case(column, post)
                if db_row[column] != "":
                    continue
                try:
                    db_row[column] = post["data"][column]
                except KeyError:
                    db_row[column] = "NULL"
                self.send_to_db(db_row, self.columns)

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        match column:
            case "created_utc":
                return str(datetime.fromtimestamp(item["data"][column]))[:10]
            case "link":
                return f"https://www.reddit.com/{item['data']['id']}"
            case "award_score":
                sum = 0
                for award in item["data"]["all_awardings"]:
                    sum += award["coin_price"] * award["count"]
                return sum
            case _:
                return ""

    def request_has_error(self, result: requests.Response) -> bool:
        return super().request_has_error(result)
