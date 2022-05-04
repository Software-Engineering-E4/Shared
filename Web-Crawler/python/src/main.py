from youtube.youtube_videos import Youtube
from reddit.reddit_comments import RedditComments
from reddit.reddit_posts import RedditPosts
from utils.DBManager import DBManager


def main() -> None:
    with DBManager("Web-Crawler/python/config/database.json") as db:
        # yt = Youtube(db)
        # queries = ["colorectal cancer", "cancer", "colorectal", "cancer colorectal"]
        # for query in queries:
        #     output = yt.request(query)
        #     yt.send_to_db(output)

        reddit_posts = RedditPosts(db)
        subreddits = [
            "cancerbiology",
            "cancerfamilysupport",
            "cancercaregivers",
            "colorectalcancer",
        ]
        for subreddit in subreddits:
            output = reddit_posts.request(subreddit)
            reddit_posts.send_to_db(output)

        reddit_comments = RedditComments(db)


if __name__ == "__main__":
    main()
