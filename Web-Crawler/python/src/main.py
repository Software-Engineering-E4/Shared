from youtube import Youtube
from reddit import Reddit
from utils.DBManager import DBManager


def main() -> None:
    with DBManager("Web-Crawler/python/config/database.json") as db:
        yt = Youtube(db)
        queries = ["colorectal cancer", "cancer", "colorectal", "cancer colorectal"]
        for query in queries:
            output = yt.request(query)
            yt.send_to_db(output)

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


if __name__ == "__main__":
    main()
