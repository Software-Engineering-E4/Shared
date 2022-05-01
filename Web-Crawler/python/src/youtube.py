import json
from datetime import datetime
from googleapiclient.discovery import build
from utils.DBManager import DBManager


class Youtube:
    def __init__(self, db: DBManager) -> None:
        self.db = db
        self.db.set_table_name("youtube_videos")
        self.api_key = ""
        self.db_columns: list[str] = []

        with open("Web-Crawler/python/config/youtube.json") as file:
            data = json.load(file)
            self.api_key = data["api_key"]
            self.db_columns = data["db_columns"]

        self.resource = build("youtube", "v3", developerKey=self.api_key)

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

        out: list[dict[str, str | int | datetime]] = []
        for item in request["items"]:
            data: dict[str, str | int | datetime] = {}
            for column in self.db_columns:
                if column == "id":
                    data[column] = item["id"]["videoId"]
                else:
                    try:
                        data[column] = item["snippet"][column]
                    except KeyError:
                        print(f"Key '{column}' not found")
                        data[column] = "NULL"
            out.append(data)

        return out

    def send_to_db(self, data: list[dict[str, str | int | datetime]]) -> None:
        for item in data:
            formatted = DBManager.format_data(item)
            self.db.insert(formatted)
