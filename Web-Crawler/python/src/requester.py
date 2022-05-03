from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any
from utils.DBManager import DBManager


class Requester(ABC):
    def __init__(self, db: DBManager) -> None:
        self.db = db
        self.table_name: str = ""
        self.columns: list[str] = []
        self.json_data: Any = None

    @abstractmethod
    def request(self, query: Any) -> list[dict[str, str | int | datetime]]:
        pass

    def set_table_name(self, table_name: str) -> None:
        self.db.set_table_name(table_name)
        self.columns = self.json_data["tables"][self.db.table_name]

    def set_config_file(self, path: str) -> None:
        self.config_file = path

    def send_to_db(self, data: list[dict[str, str | int | datetime]]) -> None:
        for item in data:
            formatted = DBManager.format_data(item)
            self.db.insert(formatted)
