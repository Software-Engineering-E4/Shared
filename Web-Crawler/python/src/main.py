import json
from youtube import Youtube
from reddit import Reddit
from utils.DBManager import DBManager


def main() -> None:
    db = None
    with open("Web-Crawler/python/config/database.json") as file:
        data = json.load(file)
        db = DBManager(
            host=data["host"],
            database=data["database"],
            user=data["user"],
            password=data["password"],
            port=data["port"],
        )
    # yt = Youtube(db)
    # queries = ["colorectal cancer", "cancer", "colorectal", "cancer colorectal"]
    # for query in queries:
    #     output = yt.request(query)
    #     yt.send_to_db(output)

    reddit = Reddit(db)
    subreddits = [
        "cancerbiology",
        "cancerfamilysupport",
        "cancercaregivers",
        "colorectalcancer",
    ]
    for subreddit in subreddits:
        output = reddit.request(subreddit)
        reddit.send_to_db(output)
    db.close()


if __name__ == "__main__":
    main()
