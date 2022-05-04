import json
from datetime import datetime
from utils.DBManager import DBManager
from youtube.youtube_requester import YoutubeRequester


class Youtube(YoutubeRequester):
    def __init__(self, db: DBManager) -> None:
        super(Youtube, self).__init__(db)
        self.set_table_name("youtube_videos")

    def request(self, query: str) -> list[dict[str, str | int | datetime]]:
        request = (
            self.resource.search()
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

        keys_not_found: set[str] = {""}
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
                        keys_not_found.add(column)
                        data[column] = "NULL"
            out.append(data)

        if len(keys_not_found):
            print(
                "Keys not found in the response:",
                " ".join(key for key in keys_not_found),
            )
        return out
