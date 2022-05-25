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

    def request(self, query: Any = None) -> None:
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

            self.treat_response(id, res)

    def treat_response(self, id: str, res: requests.Response):
        for child in res.json():
            for inner_child in child["data"]["children"]:
                db_row: dict[str, str | int] = {}

                for column in self.columns:
                    db_row[column] = self.treat_special_case(column, inner_child, id)
                    if db_row[column] != "":
                        continue

                    try:
                        db_row[column] = inner_child["data"][column]
                    except KeyError:
                        try:
                            db_row[column] = inner_child["data"][
                                self.columns[column]["actualName"]
                            ]
                        except KeyError:
                            db_row[column] = "NULL"

                if db_row["id"] != db_row["id_post"]:
                    self.send_to_db(db_row, self.columns)

    def treat_special_case(self, column: str, item: dict[str, Any], id=None) -> str:
        match column:
            case "id_post":
                return id
            case "created_utc":
                return str(datetime.fromtimestamp(item["data"][column]))[:10]
            case "award_score":
                sum = 0
                for award in item["data"]["all_awardings"]:
                    sum += award["coin_price"] * award["count"]
                return sum
            case _:
                return ""

    def request_has_error(self, result: requests.Response) -> bool:
        return super().request_has_error(result)
