from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from utils.DBManager import DBManager


@dataclass
class Requester(ABC):
    db: DBManager
    table_name: str = field(init=False)
    json_data: Any = field(init=False)
    columns: list[str] = field(init=False)
    config_file: str = field(init=False)

    @abstractmethod
    def request(self, query: Any) -> list[dict[str, str | int | datetime]]:
        pass

    @abstractmethod
    def authenticate(self, *args) -> None:
        pass

    def set_table_name(self, table_name: str) -> None:
        self.db.set_table_name(table_name)
        self.columns = self.json_data["tables"][self.db.table_name]

    def set_config_file(self, path: str) -> None:
        self.config_file = path

    def send_to_db(self, data: list[dict[str, str | int | datetime]]) -> None:
        for item in data:
            formatted = DBManager.format_data(item)
            self.db.insert(self.columns, formatted)
