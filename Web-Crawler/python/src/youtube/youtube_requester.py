from dataclasses import dataclass, field
import json
import logging
from requester import Requester
import googleapiclient.discovery


@dataclass
class YoutubeRequester(Requester):
    api_key: str = field(init=False)
    resource: googleapiclient.discovery.Resource = field(init=False)

    def __post_init__(self) -> None:
        super().__init__(self.db, logger=logging.getLogger(__name__))
        self.config_file = "Web-Crawler/python/config/youtube.json"

        with open(self.config_file) as file:
            self.json_data = json.load(file)
            self.api_key = self.json_data["api_key"]

        self.authenticate(self.api_key)

    def authenticate(self, api_key: str) -> None:
        self.resource = googleapiclient.discovery.build(
            "youtube", "v3", developerKey=api_key
        )
        self.logger.info("Finished authentication")
