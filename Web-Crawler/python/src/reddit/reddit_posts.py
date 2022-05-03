from datetime import datetime
import requests
from reddit.reddit_requester import RedditRequester
from utils.DBManager import DBManager


class RedditPosts(RedditRequester):
    def __init__(self, db: DBManager) -> None:
        super(RedditPosts, self).__init__(db)
        self.set_table_name("reddit_posts")

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

            for column in self.columns:
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
