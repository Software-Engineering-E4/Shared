from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import json
from random import random
from turtle import st
import mysql.connector
import translators as ts
from utils.utils import hamming_distance


@dataclass
class DBManager:
    path: str
    auto_connect: bool = field(default=True)
    host: str = field(init=False)
    database: str = field(init=False)
    user: str = field(init=False)
    password: str = field(init=False)
    port: str = field(init=False)
    table_name: str = field(init=False)
    connector: mysql.connector.connection_cext.CMySQLConnection = field(init=False)

    def __post_init__(self) -> None:
        with open(self.path) as file:
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

    def insert(self, columns: list[dict[str, str]]) -> None:
        pretty_columns = ", ".join([val for val in col.keys()][0] for col in columns)
        pretty_items = self.unpack_data(columns)
        try:
            statement = f"insert into {self.table_name} ({pretty_columns}) values ({pretty_items})"
            self.cursor.execute(statement)
        except mysql.connector.errors.IntegrityError as err:
            print(err)
        self.connector.commit()

    def execute(self, statement: str) -> None:
        try:
            self.cursor.execute(statement)
        except Exception as ex:
            print(ex)

    def format_data(
        self, response: dict[str, str | int | datetime], format
    ) -> list[dict[str, str]]:
        out: list[dict[str, str]] = []
        translations: list[dict[str, str]] = []

        for key in response.keys():
            if format[key]["type"] == "string":
                clean_str = str(response[key]).replace("'", "").replace('"', "")

                if clean_str != "NULL":
                    if format[key]["translate"] and clean_str:
                        translated = str(ts.google(
                            clean_str,
                            sleep_seconds=0.125,
                            if_ignore_limit_of_length=True,
                        ))
                        if hamming_distance(clean_str, translated)> len(clean_str)*.2:
                            translations.append({f"{key}_translated": str(translated)})
                    out.append({key: clean_str})
                else:
                    out.append({key: "NULL"})

            else:
                out.append({key: str(response[key])})

        return out + translations

    def unpack_data(self, data: list[dict[str, str]]) -> str:
        out = ""

        for row in data:
            for val in row.values():
                if val != "NULL":
                    if isinstance(val, int):
                        out += f"{val}, "
                    else:
                        out += f"'{val}', "
                else:
                    out += "NULL, "

        return out[:-2]

    def clean_translation(self, item: list[dict[str, str]]) -> list[dict[str, str]]:
        clean: list[dict[str, str]] = []

        for row in item:
            tmp: dict[str, str] = {}
            for val in row:
                tmp[val] = row[val].replace("'", "").replace('"', "")
            clean.append(tmp)
        return clean
