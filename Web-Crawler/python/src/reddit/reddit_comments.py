from dataclasses import dataclass
from datetime import datetime
import random
import string
from typing import Any
import requests
from reddit.reddit_requester import RedditRequester


@dataclass
class RedditComments(RedditRequester):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.set_table_name("reddit_comments")

    def request(self, query: Any = None) -> list[dict[str, str | int]]:
        out = []
        for values in self.db.query("reddit_posts", ["id", "subreddit"])[:100]:
            id, subreddit = values
            data: dict[str, str | int] = {}
            try:
                res = requests.get(
                    f"https://oauth.reddit.com/r/{subreddit}/comments/{id}",
                    headers=self.headers,
                    params={"limit": "100"},
                )
            except Exception as ex:
                self.logger.exception(ex)
                continue

            for child in res.json():
                for inner_child in child["data"]["children"]:
                    for column in self.columns:
                        data[column] = self.treat_special_case(column, inner_child)
                        if data[column]:
                            continue
                        try:
                            data[column] = inner_child["data"][column]
                        except KeyError:
                            try:
                                data[column] = inner_child["data"][
                                    self.columns[column]["actualName"]
                                ]
                            except KeyError:
                                data[column] = "NULL"
                    out.append(data)

            self.logger.info(f"Comments with post_id={id} done")

        return out

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        match column:
            case "id":
                return "".join(
                    random.choice(string.ascii_lowercase + string.digits)
                    for _ in range(10)
                )
            case "id_post":
                return item["data"]["id"]
            case "created_utc":
                return str(datetime.fromtimestamp(item["data"][column]))[:10]
            case _:
                return ""
