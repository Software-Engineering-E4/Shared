from dataclasses import dataclass
from datetime import datetime
import logging
from typing import Any
from utils.DBManager import DBManager
from youtube.youtube_requester import YoutubeRequester


@dataclass
class YoutubeComments(YoutubeRequester):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.logger = logging.getLogger(__name__)
        self.set_table_name("youtube_comments")

    def request(self, query: Any = None) -> list[dict[str, str | int]]:
        return super().request(query)

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        return ""
