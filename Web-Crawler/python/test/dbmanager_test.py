import unittest
from utils.DBManager import DBManager
import mysql.connector


class DBManagerTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.db = DBManager("Web-Crawler/python/config/database.json", False)
        super().__init__(methodName)

    def test_wrong_credentials(self) -> None:
        self.assertRaises(mysql.connector.errors.DatabaseError, self.db.make_connection, "", "", "", "", "3306")
