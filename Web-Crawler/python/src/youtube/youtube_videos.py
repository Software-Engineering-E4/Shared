from dataclasses import dataclass
import logging
from typing import Any
from youtube.youtube_requester import YoutubeRequester


@dataclass
class YoutubeVideos(YoutubeRequester):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.logger = logging.getLogger(__name__)
        self.set_table_name("youtube_videos")

    def request(self, query: str) -> list[dict[str, str | int]]:
        request = (
            self.resource.search()  # type: ignore
            .list(
                part="snippet",
                order="relevance",
                q=query,
                maxResults="50",
                type="video",
                # location=(38.11295, -102.30703),
                # locationRadius=(1000 km)
            )
            .execute()
        )

        out: list[dict[str, str | int]] = []
        for item in request["items"]:
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
