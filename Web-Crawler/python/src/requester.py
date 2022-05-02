from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any
from utils.DBManager import DBManager


class Requester(ABC):
    def __init__(self, db: DBManager) -> None:
        self.db = db
        self.db_columns: list[str] = []

    @abstractmethod
    def request(self, query: Any) -> list[dict[str, str | int | datetime]]:
        pass

    def send_to_db(self, data: list[dict[str, str | int | datetime]]) -> None:
        for item in data:
            formatted = DBManager.format_data(item)
            self.db.insert(formatted)
