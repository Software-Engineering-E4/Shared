from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from utils.DBManager import DBManager
import logging
import requests


class SendMode(Enum):
    AUTO = 0
    INSERT = 1
    UPDATE = 2

    def __eq__(self, o: object) -> bool:
        try:
            return self.value == SendMode(o).value and self.name == SendMode(o).name
        except:
            return False


@dataclass
class Requester(ABC):
    db: DBManager
    link: str = ""
    real_time: bool = True
    send_mode: SendMode = SendMode.AUTO
    table_name: str = field(init=False)
    json_data: Any = field(init=False)
    columns: dict[str, dict[str, str]] = field(init=False)
    config_file: str = field(init=False)
    logger: logging.Logger = field(default=logging.getLogger(__name__), init=False)

    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s %(name)s line %(lineno)s: %(message)s",
        filename="latest.log",
    )

    @abstractmethod
    def request(self, query: Any) -> list[dict[str, str | int]]:
        pass

    @abstractmethod
    def authenticate(self, *args) -> None:
        pass

    def set_table_name(self, table_name: str) -> None:
        self.db.set_table_name(table_name)
        self.columns = self.json_data["tables"][self.db.table_name]

    def send_to_db(self, data: list[dict[str, str | int]], format) -> None:
        for item in data:
            formatted = self.db.format_data(item, format)
            formatted = self.db.clean_translation(formatted)

            match self.send_mode:
                case SendMode.AUTO:
                    ids = self.db.query_one(self.db.table_name, "id")
                    if item["id"] in ids:
                        self.db.update(formatted)
                    else:
                        self.db.insert(formatted)
                case SendMode.INSERT:
                    self.db.insert(formatted)
                case SendMode.UPDATE:
                    self.db.update(formatted)
                case _:
                    continue

            self.logger.debug(f"{self.send_mode.__str__()} on row with id={item['id']}")

    @abstractmethod
    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        pass

    @staticmethod
    def build(params: dict[str, str]) -> str:
        return "&".join(f"{param}={params[param]}" for param in params.keys())

    @abstractmethod
    def request_has_error(self, result: requests.Response) -> bool:
        pass
