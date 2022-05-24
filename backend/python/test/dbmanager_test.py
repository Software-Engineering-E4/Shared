import socket
import unittest
from utils.DBManager import DBManager
import mysql.connector


class DBManagerTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.db = DBManager("backend/config/database.json", False)
        super().__init__(methodName)

    def internet_connection(self) -> None:
        sock = None
        try:
            sock = socket.create_connection(("1.1.1.1", 53))
        except TimeoutError:
            self.assertTrue(False, "No internet connection")
        self.assertIsNotNone(sock, "No internet connection")

    def test_wrong_credentials(self) -> None:
        self.assertRaises(
            mysql.connector.errors.DatabaseError,
            self.db.make_connection,
            "",
            "",
            "",
            "",
            "3306",
        )

    def test_reddit_posts_mock_values(self) -> None:
        self.db.connector = self.db.make_connection(
            self.db.database, self.db.user, self.db.password, self.db.host, self.db.port
        )
        self.db.set_table_name("reddit_posts")
        self.db.insert(
            {"id": "mock1234", "selftext": "mocktext", "title": "mock title"}
        )
        self.db.update(
            {"id": "mock1234", "selftext": "mocktext", "title": "mock updated title"}
        )
        self.db.execute("delete from reddit_posts where id=mock1234")

    def test_reddit_comments_mock_values(self) -> None:
        self.db.connector = self.db.make_connection(
            self.db.database, self.db.user, self.db.password, self.db.host, self.db.port
        )
        self.db.set_table_name("reddit_comments")
        self.db.insert({"id": "mock1234", "selftext": "mocktext", "title": "mocktitle"})
        self.db.update(
            {"id": "mock1234", "selftext": "mocktext", "title": "mock updated title"}
        )
        self.db.execute("delete from reddit_comments where id=mock1234")

    def test_youtube_videos_mock_values(self) -> None:
        self.db.connector = self.db.make_connection(
            self.db.database, self.db.user, self.db.password, self.db.host, self.db.port
        )
        self.db.set_table_name("youtube_videos")
        self.db.insert({"id": "mock1234", "selftext": "mocktext", "title": "mocktitle"})
        self.db.update(
            {"id": "mock1234", "selftext": "mocktext", "title": "mock updated title"}
        )
        self.db.execute("delete from youtube_videos where id=mock1234")

    def test_youtube_comments_mock_values(self) -> None:
        self.db.connector = self.db.make_connection(
            self.db.database, self.db.user, self.db.password, self.db.host, self.db.port
        )
        self.db.set_table_name("youtube_comments")
        self.db.insert({"id": "mock1234", "selftext": "mocktext", "title": "mocktitle"})
        self.db.update(
            {"id": "mock1234", "selftext": "mocktext", "title": "mock updated title"}
        )
        self.db.execute("delete from youtube_comments where id=mock1234")

    def test_twitter_posts_mock_values(self) -> None:
        self.db.connector = self.db.make_connection(
            self.db.database, self.db.user, self.db.password, self.db.host, self.db.port
        )
        self.db.set_table_name("twitter_posts")
        self.db.insert({"id": "mock1234", "selftext": "mocktext", "title": "mocktitle"})
        self.db.update(
            {"id": "mock1234", "selftext": "mocktext", "title": "mock updated title"}
        )
        self.db.execute("delete from twitter_posts where id=mock1234")
