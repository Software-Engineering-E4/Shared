from utils.DBManager import DBManager
from reddit.reddit_posts import RedditPosts
from reddit.reddit_comments import RedditComments
from youtube.youtube_videos import YoutubeVideos
from youtube.youtube_comments import YoutubeComments


def main() -> None:
    with DBManager("backend/python/config/database.json", translate=True) as db:
        youtube_videos = YoutubeVideos(db)
        queries = ["colorectal cancer", "cancer", "colorectal", "cancer colorectal"]
        for query in queries:
            output = youtube_videos.request(query)
            youtube_videos.send_to_db(output, youtube_videos.columns)

        youtube_comments = YoutubeComments(db)
        response = youtube_comments.request()
        youtube_comments.send_to_db(response, youtube_comments.columns)

        reddit_posts = RedditPosts(db)
        subreddits = [
            "cancerbiology",
            "cancerfamilysupport",
            "cancercaregivers",
            "colorectalcancer",
        ]
        for subreddit in subreddits:
            output = reddit_posts.request(subreddit)
            reddit_posts.send_to_db(output, reddit_posts.columns)

        reddit_comments = RedditComments(db)
        response = reddit_comments.request()
        reddit_comments.send_to_db(response, reddit_comments.columns)


if __name__ == "__main__":
    main()
