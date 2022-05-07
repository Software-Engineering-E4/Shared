from dataclasses import dataclass
from datetime import datetime
from typing import Any
from utils.DBManager import DBManager
from youtube.youtube_requester import YoutubeRequester


@dataclass
class YoutubeComments(YoutubeRequester):
    db: DBManager

    def __post_init__(self) -> None:
        self.db.set_table_name("youtube_comments")

    def request(self, query: Any) -> list[dict[str, str | int | datetime]]:
        return super().request(query)

    def send_to_db(self, data: list[dict[str, str | int | datetime]]) -> None:
        return

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        return ""
