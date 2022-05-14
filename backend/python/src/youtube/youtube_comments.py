from dataclasses import dataclass
import logging
from typing import Any
from utils.DBManager import DBManager
from youtube.youtube_requester import YoutubeRequester
import requests


@dataclass
class YoutubeComments(YoutubeRequester):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.logger = logging.getLogger(__name__)
        self.set_table_name("youtube_comments")

    def request(self, query: Any = None) -> list[dict[str, str | int]]:
        out: list[dict[str, str | int]] = []
        for id in self.db.query_one("youtube_videos", "id"):
            request_params = self.build(
                {
                    "key": self.api_key,
                    "part": "snippet",
                    "videoId": id,
                    "maxResults": "100",
                    "textFormat": "plainText",
                    "order": "relevance",
                }
            )
            res = requests.get(f"{self.link}/commentThreads?{request_params}")
            if self.request_has_error(res):
                continue

            for result in res.json()["items"]:
                inner_data = result["snippet"]["topLevelComment"]
                data: dict[str, str | int] = {}

                for column in self.columns:
                    data[column] = self.treat_special_case(column, inner_data)
                    if data[column] != "":
                        continue

                    try:
                        data[column] = inner_data["snippet"][column]
                    except KeyError:
                        try:
                            data[column] = inner_data["snippet"][
                                self.columns[column]["actualName"]
                            ]
                        except KeyError:
                            data[column] = "NULL"

                if self.real_time:
                    self.send_to_db([data], self.columns)
                else:
                    out.append(data)
            if not self.real_time:
                self.logger.debug(f"Comments with video_id={id} done")

        return out

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        match column:
            case "id":
                return item["id"]
            case "created_utc":
                return item["snippet"]["publishedAt"][:10]
            case _:
                return ""
