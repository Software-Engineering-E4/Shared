from datetime import datetime
import json
import requests
from utils.DBManager import DBManager


class Reddit:
    def __init__(self, db: DBManager) -> None:
        self.db = db
        self.db.set_table_name("reddit_posts")
        self.username = ""
        self.password = ""
        self.client_id = ""
        self.secret_key = ""
        self.db_columns: list[str] = []

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

        out: list[dict[str, str | int | datetime]] = []
        for post in res.json()["data"]["children"]:
            data: dict[str, str | int | datetime] = {}

            for column in self.db_columns:
                if column == "created_utc":
                    data[column] = datetime.fromtimestamp(post["data"][column])
                else:
                    try:
                        data[column] = post["data"][column]
                    except KeyError:
                        print(f"Key '{column}' not found")
                        data[column] = "NULL"
            out.append(data)

        return out

    def send_to_db(self, data: list[dict[str, str | int | datetime]]) -> None:
        for item in data:
            formatted = DBManager.format_data(item)
            self.db.insert(formatted)
            # val = f"""update {self.db.table_name} set created_utc='{str(item["created_utc"])}' where id='{item["id"]}'"""
            # self.db.execute(val)
