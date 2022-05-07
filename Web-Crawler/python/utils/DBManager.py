from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import json
from logging import Logger
import logging
from random import random
from turtle import st
import mysql.connector
import translators as ts
from Levenshtein import distance as lv


@dataclass
class DBManager:
    config_file: str
    auto_connect: bool = field(default=True)
    host: str = field(init=False)
    database: str = field(init=False)
    user: str = field(init=False)
    password: str = field(init=False)
    port: str = field(init=False)
    table_name: str = field(init=False)
    connector: mysql.connector.connection_cext.CMySQLConnection = field(init=False)
    logger:logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

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
        return sql_connection

    def __enter__(self) -> DBManager:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.connector.commit()
        self.connector.close()

    def set_table_name(self, table_name: str) -> None:
        self.table_name = table_name

    def insert(self, columns: dict[str, str | int]) -> None:
        pretty_columns = ", ".join(col for col in columns.keys())
        pretty_items = self.unpack_for_insert(columns)
        statement = (
            f"insert into {self.table_name} ({pretty_columns}) values ({pretty_items})"
        )
        try:
            self.cursor.execute(statement)
        except mysql.connector.errors.IntegrityError as err:
            self.logger.info(err)
        self.connector.commit()

    def update(self, columns: dict[str, str | int]) -> None:
        result = self.unpack_for_update(columns)
        for col in columns.values():
            statement = f"update {self.table_name} set {result} where id='{col}'"
            try:
                self.cursor.execute(statement)
            except mysql.connector.errors.IntegrityError as err:
                self.logger.info(err)
        self.connector.commit()

    def execute(self, statement: str) -> None:
        try:
            self.cursor.execute(statement)
        except Exception as ex:
            self.logger.info(ex)

    def format_data(
        self, response: dict[str, str | int | datetime], format
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

                if clean_str != "NULL":
                    if format[key]["translate"] and clean_str:
                        translated = str(
                            ts.google(
                                clean_str,
                                sleep_seconds=0.125,
                                if_ignore_limit_of_length=True,
                            )
                        )
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
                    out[key]= int(str(response[key]))
                else:
                    out[key] = "NULL"

        for key in translations.keys():
            out[key] = translations[key]
        return out

    def unpack_for_insert(self, data: dict[str, str | int]) -> str:
        out = ""

        for row in data:
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
            else:
                out += f"{row}=NULL, "

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
