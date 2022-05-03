import json
from typing import Any
import requests
from requester import Requester
from utils.DBManager import DBManager


class RedditRequester(Requester):
    def __init__(self, db: DBManager) -> None:
        super().__init__(db)
        self.set_config_file("Web-Crawler/python/config/reddit.json")

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
