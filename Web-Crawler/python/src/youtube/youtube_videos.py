from dataclasses import dataclass
from datetime import datetime
from youtube.youtube_requester import YoutubeRequester


@dataclass
class YoutubeVideos(YoutubeRequester):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.set_table_name("youtube_videos")

    def request(self, query: str) -> list[dict[str, str | int | datetime]]:
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

        out: list[dict[str, str | int | datetime]] = []
        for item in request["items"]:
            data: dict[str, str | int | datetime] = {}

            for column in self.columns:
                if column == "id":
                    data[column] = item["id"]["videoId"]
                else:
                    try:
                        data[column] = item["snippet"][column]
                    except KeyError:
                        data[column] = "NULL"

            out.append(data)

        return out
