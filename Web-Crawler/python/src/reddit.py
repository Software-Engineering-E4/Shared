from datetime import datetime
import json
import requests
from utils.DBManager import DBManager
from src.requester import Requester


class Reddit(Requester):
    def __init__(self, db: DBManager) -> None:
        super(Reddit, self).__init__(db)
        self.db.set_table_name("reddit_posts")
        self.username = ""
        self.password = ""
        self.client_id = ""
        self.secret_key = ""

        with open("Web-Crawler/python/config/reddit.json") as file:
            data = json.load(file)
            account = data["authentication"]
            self.username, self.password, self.client_id, self.secret_key = (
                account["username"],
                account["password"],
                account["client_id"],
                account["secret_key"],
            )
            self.db_columns = data["db_columns"]

        auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret_key)  # type: ignore

        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
        }
        self.headers = {"User-Agent": "MyAPI/0.0.1"}
        res = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=auth,
            data=data,
            headers=self.headers,
        )
        TOKEN = res.json()["access_token"]
        self.headers["Authorization"] = f"bearer {TOKEN}"

    def request(self, subreddit: str) -> list[dict[str, str | int | datetime]]:
        res = requests.get(
            f"https://oauth.reddit.com/r/{subreddit}/hot",
            headers=self.headers,
            params={"limit": "100"},
        )

        keys_not_found: set[str] = {""}
        out: list[dict[str, str | int | datetime]] = []
        for post in res.json()["data"]["children"]:
            data: dict[str, str | int | datetime] = {}

            for column in self.db_columns:
                if column == "created_utc":
                    data[column] = str(datetime.fromtimestamp(post["data"][column]))[:10]
                else:
                    try:
                        data[column] = post["data"][column]
                    except KeyError:
                        keys_not_found.add(column)
                        data[column] = "NULL"
            out.append(data)

        if len(keys_not_found):
            print("Keys not found in the response:", " ".join(key for key in keys_not_found))
        return out

    def send_to_db(self, data: list[dict[str, str | int | datetime]]) -> None:
        for item in data:
            formatted = DBManager.format_data(item)
            self.db.insert(formatted)
            # val = f"""update {self.db.table_name} set created_utc='{str(item["created_utc"])}' where id='{item["id"]}'"""
            # self.db.execute(val)
