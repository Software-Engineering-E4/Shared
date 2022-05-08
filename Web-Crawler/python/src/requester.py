from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from utils.DBManager import DBManager
import logging


class SendMode(Enum):
    AUTO = (0,)
    INSERT = (1,)
    UPDATE = (2,)


@dataclass
class Requester(ABC):
    db: DBManager
    table_name: str = field(init=False)
    json_data: Any = field(init=False)
    columns: dict[str, dict[str, str]] = field(init=False)
    config_file: str = field(init=False)
    logger: logging.Logger = logging.getLogger()
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(name)s line %(lineno)s: %(message)s",
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

    def send_to_db(
        self, data: list[dict[str, str | int]], format, mode: SendMode = SendMode.AUTO
    ) -> None:
        for item in data:
            formatted = self.db.format_data(item, format)
            formatted = self.db.clean_translation(formatted)

            match mode:
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

            self.logger.info(f"{mode.__str__()} on row with id={item['id']}")

    @abstractmethod
    def treat_special_case(self, column: str, item: dict[str, Any]) -> str:
        pass
