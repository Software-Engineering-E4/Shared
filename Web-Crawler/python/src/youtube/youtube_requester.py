import json
from requester import Requester
from utils.DBManager import DBManager
from googleapiclient.discovery import build


class YoutubeRequester(Requester):
    def __init__(self, db: DBManager) -> None:
        super().__init__(db)
        self.set_config_file("Web-Crawler/python/config/youtube.json")

        with open(self.config_file) as file:
            self.json_data = json.load(file)
            self.api_key = self.json_data["api_key"]

        self.authenticate(self.api_key)

    def authenticate(self, api_key: str) -> None:
        self.resource = build("youtube", "v3", developerKey=api_key)
