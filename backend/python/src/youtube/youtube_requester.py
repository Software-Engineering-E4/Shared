from dataclasses import dataclass, field
import json
from requester import Requester
import googleapiclient.discovery
import requests


@dataclass
class YoutubeRequester(Requester):
    api_key: str = field(init=False)
    access_token: str = field(init=False)
    resource: googleapiclient.discovery.Resource = field(init=False)

    def __post_init__(self) -> None:
        super().__init__(self.db, "https://www.googleapis.com/youtube/v3", self.send_mode)
        self.config_file = "backend/config/youtube.json"

        with open(self.config_file) as file:
            self.json_data = json.load(file)
            self.api_key = self.json_data["authentication"]["api_key"]

        self.authenticate(self.api_key)

    def authenticate(self, api_key: str) -> None:
        self.resource = googleapiclient.discovery.build(
            "youtube", "v3", developerKey=api_key
        )
        self.logger.info("Finished authentication")

    def request_has_error(self, result: requests.Response) -> bool:
        try:
            result.json()["error"]
            try:
                self.logger.error(
                    f"Skipping request, reason: {result.json()['error']['errors'][0]['message']}"
                )
            except KeyError:
                try:
                    self.logger.error(f"Skipping request, reason: {result.json()['error']['message']}")
                except KeyError:
                    self.logger.error(f"Skipped request, reason: unknown {result.json()}")
            return True
        except KeyError:
            return False
