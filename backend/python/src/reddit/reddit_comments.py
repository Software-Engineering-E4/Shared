from dataclasses import dataclass
from datetime import datetime
import logging
from typing import Any
import requests
from reddit.reddit_requester import RedditRequester


@dataclass
class RedditComments(RedditRequester):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.logger = logging.getLogger(__name__)
        self.set_table_name("reddit_comments")

    def request(self, query: Any = None) -> list[dict[str, str | int]]:
        out: list[dict[str, str | int]] = []
        for values in self.db.query("reddit_posts", ["id", "subreddit"]):
            id, subreddit = values
            try:
                res = requests.get(
                    f"{self.link}/{subreddit}/comments/{id}",
                    headers=self.headers,
                    params={"limit": "100"},
                )
            except Exception as ex:
                self.logger.exception(ex)
                continue

            for child in res.json():
                for inner_child in child["data"]["children"]:
                    data: dict[str, str | int] = {}
                    for column in self.columns:
                        data[column] = self.treat_special_case(column, inner_child, id)
                        if data[column] != "":
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
                    if data["id"] != data["id_post"]:
                        out.append(data)
                        if self.real_time:
                            self.send_to_db([data], self.columns)
            if not self.real_time:
                self.logger.info(f"Comments with post_id={id} done")

        return out

    def treat_special_case(self, column: str, item: dict[str, Any], id=None) -> str:
        match column:
            case "id_post":
                return id
            case "created_utc":
                return str(datetime.fromtimestamp(item["data"][column]))[:10]
            case _:
                return ""
