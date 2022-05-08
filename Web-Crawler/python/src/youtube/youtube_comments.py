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

    def request(self, query: Any = None) -> list[dict[str, str | int]]:
        return super().request(query)

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        return ""
