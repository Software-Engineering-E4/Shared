from dataclasses import dataclass, field
import json
import logging
import requests
from requester import Requester


@dataclass
class RedditRequester(Requester):
    username: str = field(init=False)
    password: str = field(init=False)
    client_id: str = field(init=False)
    secret_key: str = field(init=False)
    headers: dict[str, str] = field(init=False)

    def __post_init__(self) -> None:
        super().__init__(self.db, "https://oauth.reddit.com/r", self.real_time, self.send_mode)
        self.config_file = "backend/python/config/reddit.json"

        with open(self.config_file) as file:
            self.json_data = json.load(file)
            account = self.json_data["authentication"]
            self.username, self.password, self.client_id, self.secret_key = (
                account["username"],
                account["password"],
                account["client_id"],
                account["secret_key"],
            )
        self.authenticate(self.client_id, self.secret_key, self.username, self.password)

    def authenticate(
        self, client_id: str, secret_key: str, username: str, password: str
    ) -> None:
        auth = requests.auth.HTTPBasicAuth(client_id, secret_key)  # type: ignore

        data = {
            "grant_type": "password",
            "username": username,
            "password": password,
        }
        self.headers = {"User-Agent": "MyAPI/0.0.1"}
        res = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=auth,
            data=data,
            headers=self.headers,
        )
        token = res.json()["access_token"]
        self.headers["Authorization"] = f"bearer {token}"
        self.logger.info("Finished authentication")
