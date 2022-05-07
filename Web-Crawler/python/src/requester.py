from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from utils.DBManager import DBManager


@dataclass
class Requester(ABC):
    db: DBManager
    translate: bool = field(default=False)
    table_name: str = field(init=False)
    json_data: Any = field(init=False)
    columns: dict[str, dict[str, str]] = field(init=False)
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

    def send_to_db(self, data: list[dict[str, str | int | datetime]], format) -> None:
        for item in data:
            formatted = self.db.format_data(item, format)
            formatted = self.db.clean_translation(formatted)
            # self.db.insert(formatted)
            self.db.update(formatted)

    @abstractmethod
    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        pass
