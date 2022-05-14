from dataclasses import dataclass
import logging
from typing import Any
from youtube.youtube_requester import YoutubeRequester
import requests


@dataclass
class YoutubeVideos(YoutubeRequester):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.logger = logging.getLogger(__name__)
        self.set_table_name("youtube_videos")

    def request(self, query: str) -> list[dict[str, str | int]]:
        out: list[dict[str, str | int]] = []
        for year in range(2015, 2018):
            for month in range(1, 13):
                is_next_year = (month + 1) == 13
                request_params = self.build(
                    {
                        "key": self.api_key,
                        "part": "snippet",
                        "maxResults": "50",
                        "q": query,
                        "publishedAfter": f"{year}-{month}-01T00:00:00Z",
                        "publishedBefore": f"{year + is_next_year}-{month + 1 - is_next_year * 12}-01T00:00:00Z",
                        "type": "video",
                    }
                )
                self.logger.debug(f"Requesting query='{query}', year={year}, month={month}")
                result = requests.get(f"{self.link}/search?{request_params}")
                if self.request_has_error(result):
                    continue

                for item in result.json()["items"]:
                    data: dict[str, str | int] = {}

                    for column in self.columns:
                        data[column] = self.treat_special_case(column, item)
                        if data[column]:
                            continue
                        try:
                            data[column] = item["snippet"][column]
                        except KeyError:
                            try:
                                data[column] = item["snippet"][
                                    self.columns[column]["actualName"]
                                ]
                            except KeyError:
                                data[column] = "NULL"

                    if self.real_time:
                        self.send_to_db([data], self.columns)
                    else:
                        out.append(data)

        return out

    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        match column:
            case "id":
                return item["id"]["videoId"]
            case "thumbnail":
                return item["snippet"]["thumbnails"]["high"]["url"]
            case "link":
                return f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            case _:
                return ""
