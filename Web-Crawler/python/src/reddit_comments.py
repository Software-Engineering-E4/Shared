import datetime
from typing import Any
from utils.DBManager import DBManager
from requester import Requester


class RedditComments(Requester):
    def __init__(self, db: DBManager) -> None:
        super(RedditComments, self).__init__(db)
        self.db.set_table_name("reddit_comments")

    def request(self, query: Any) -> list[dict[str, str | int | datetime]]:
        return super().request(query)

    def send_to_db(self, data: list[dict[str, str | int | datetime]]) -> None:
        return
