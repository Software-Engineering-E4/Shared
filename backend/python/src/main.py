import logging
from utils.DBManager import DBManager
from reddit.reddit_posts import RedditPosts
from reddit.reddit_comments import RedditComments
from youtube.youtube_videos import YoutubeVideos
from youtube.youtube_comments import YoutubeComments


def main() -> None:
    with DBManager("backend/config/database.json", translate=True) as db:
        youtube_videos = YoutubeVideos(db)
        queries = ["colorectal cancer", "cancer", "colorectal", "cancer colorectal"]
        for query in queries:
            youtube_videos.request(query)

        youtube_comments = YoutubeComments(db)
        youtube_comments.request()

        reddit_posts = RedditPosts(db)
        subreddits = [
            "cancerbiology",
            "cancerfamilysupport",
            "cancercaregivers",
            "colorectalcancer",
            "Fuckcancer",
            "CancerAdvances",
        ]
        for subreddit in subreddits:
            reddit_posts.request(subreddit)

        reddit_comments = RedditComments(db)
        reddit_comments.request()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s %(name)s line %(lineno)s: %(message)s",
        filename="latest.log",
    )
    main()
