from __future__ import annotations
import json
import logging
from dataclasses import dataclass, field
import mysql.connector
import translators as ts
from Levenshtein import distance as lv


@dataclass
class DBManager:
    config_file: str
    auto_connect: bool = field(default=True)
    translate: bool = field(default=False)
    host: str = field(init=False)
    database: str = field(init=False)
    user: str = field(init=False)
    password: str = field(init=False)
    port: str = field(init=False)
    table_name: str = field(init=False)
    connector: mysql.connector.connection_cext.CMySQLConnection = field(
        init=False, default=mysql.connector.connection_cext.CMySQLConnection()
    )
    logger: logging.Logger = field(default=logging.getLogger(__name__), init=False)

    def __post_init__(self) -> None:
        with open(self.config_file) as file:
            data = json.load(file)
            self.host = data["host"]
            self.database = data["database"]
            self.user = data["user"]
            self.password = data["password"]
            self.port = data["port"]
            self.table_name = ""

        if self.auto_connect:
            self.connector = self.make_connection(
                self.database, self.user, self.password, self.host, self.port
            )

    def make_connection(
        self, database: str, user: str, password: str, host: str, port: str
    ) -> mysql.connector.connection_cext.CMySQLConnection:
        sql_connection = mysql.connector.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        self.cursor = sql_connection.cursor()
        self.logger.info(f"Connected to the database, {self.__repr__()}")
        return sql_connection

    def __enter__(self) -> DBManager:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.connector.commit()
        self.connector.close()

    def __repr__(self) -> str:
        return f"""{__name__}(config_file='{self.config_file}', auto_connect={self.auto_connect}, \
translate={self.translate}, host='{self.host}', database='{self.database}', user='{self.user}', \
password='{self.password}', port='{self.port}')"""

    def set_table_name(self, table_name: str) -> None:
        self.table_name = table_name

    def insert(self, columns: dict[str, str | int]) -> None:
        pretty_columns = ", ".join(col for col in columns.keys())
        pretty_items = self.unpack_for_insert(columns)
        statement = (
            f"insert into {self.table_name} ({pretty_columns}) values ({pretty_items})"
        )
        self.logger.debug(f"Insert: {statement}")
        try:
            self.cursor.execute(statement)
        except mysql.connector.errors.Error as err:
            self.logger.exception(err)
        self.connector.commit()

    def update(self, columns: dict[str, str | int]) -> None:
        result = self.unpack_for_update(columns)
        statement = f"update {self.table_name} set {result} where id='{columns['id']}'"
        self.logger.debug(f"Update: {statement}")
        try:
            self.cursor.execute(statement)
        except mysql.connector.errors.Error as err:
            self.logger.exception(err)
        self.connector.commit()

    def query(self, table_name: str, items: list[str]) -> list[tuple[str, ...]]:
        pretty_items = ", ".join(item for item in items)
        self.cursor.execute(f"select {pretty_items} from {table_name}")
        return self.cursor.fetchall()

    def query_one(self, table_name: str, item: str) -> set[str]:
        self.cursor.execute(f"select {item} from {table_name}")
        return set(ele[0] for ele in self.cursor.fetchall())

    def execute(self, statement: str) -> None:
        try:
            self.cursor.execute(statement)
        except Exception as ex:
            self.logger.exception(ex)

    def format_data(
        self, response: dict[str, str | int], format
    ) -> dict[str, str | int]:
        out: dict[str, str | int] = {}
        translations: dict[str, str | int] = {}

        for key in response.keys():
            if format[key]["type"] == "string":
                clean_str = (
                    str(response[key])
                    .replace("'", "")
                    .replace('"', "")
                    .replace("\n", "")
                    .strip()
                )
                if clean_str == "":
                    clean_str = "NULL"
                if clean_str != "NULL":
                    if format[key]["translate"] and clean_str != "" and self.translate:
                        if len(clean_str) >= 5000:
                            continue
                        try:
                            translated = str(
                                ts.google(
                                    clean_str,
                                    sleep_seconds=0.06,
                                    if_ignore_limit_of_length=True,
                                )
                            )
                        except Exception as ex:
                            self.logger.exception(ex)
                            continue
                        if (
                            lv(clean_str, translated) > len(clean_str) * 0.2
                            and clean_str.find(translated) != 0
                        ):
                            translations[f"{key}_translated"] = str(translated)
                    out[key] = clean_str
                else:
                    out[key] = "NULL"
            elif format[key]["type"] == "date":
                out[key] = str(response[key])[:10]
            else:
                if response[key] != "NULL":
                    out[key] = int(str(response[key]))
                else:
                    out[key] = "NULL"

        for key in translations.keys():
            out[key] = translations[key]
        return out

    def unpack_for_insert(self, data: dict[str, str | int]) -> str:
        out = ""

        for row in data.values():
            if row != "NULL":
                if isinstance(row, int):
                    out += f"{row}, "
                else:
                    out += f"'{row}', "
            else:
                out += "NULL, "

        return out[:-2]

    def unpack_for_update(self, data: dict[str, str | int]) -> str:
        out = ""

        for row in data.keys():
            if data[row] != "NULL":
                if isinstance(data[row], int):
                    out += f"{row}={data[row]}, "
                else:
                    out += f"{row}='{data[row]}', "

        return out[:-2]

    def clean_translation(self, item: dict[str, str | int]) -> dict[str, str | int]:
        clean: dict[str, str | int] = {}

        for row in item:
            if isinstance(item[row], str):
                clean[row] = (
                    str(item[row])
                    .replace("'", "")
                    .replace('"', "")
                    .replace("\n", "")
                    .strip()
                )
            else:
                clean[row] = item[row]
        return clean
