from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import json
from random import random
from turtle import st
import mysql.connector
import translators as ts
from Levenshtein import distance as lv


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

    def insert(self, columns: list[dict[str, str | int]]) -> None:
        pretty_columns = ", ".join([val for val in col.keys()][0] for col in columns)
        pretty_items = self.unpack_for_insert(columns)
        statement = (
            f"insert into {self.table_name} ({pretty_columns}) values ({pretty_items})"
        )
        try:
            self.cursor.execute(statement)
        except mysql.connector.errors.IntegrityError as err:
            print(err)
        self.connector.commit()

    def update(self, columns: list[dict[str, str | int]]) -> None:
        result = self.unpack_for_update(columns)
        for col in columns[0].values():
            statement = f"update {self.table_name} set {result} where id='{col}'"
            try:
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
    ) -> list[dict[str, str | int]]:
        out: list[dict[str, str | int]] = []
        translations: list[dict[str, str | int]] = []

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
                            translations.append({f"{key}_translated": str(translated)})
                    out.append({key: clean_str})
                else:
                    out.append({key: "NULL"})
            elif format[key]["type"] == "date":
                out.append({key: str(response[key])[:10]})
            else:
                if response[key] != "NULL":
                    out.append({key: int(response[key])})  # type: ignore
                else:
                    out.append({key: "NULL"})

        return out + translations

    def unpack_for_insert(self, data: list[dict[str, str | int]]) -> str:
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

    def unpack_for_update(self, data: list[dict[str, str | int]]) -> str:
        out = ""

        for row in data:
            for val in row.keys():
                if row[val] != "NULL":
                    if isinstance(row[val], int):
                        out += f"{val}={row[val]}, "
                    else:
                        out += f"{val}='{row[val]}', "
                else:
                    out += f"{val}=NULL, "

        return out[:-2]

    def clean_translation(
        self, item: list[dict[str, str | int]]
    ) -> list[dict[str, str | int]]:
        clean: list[dict[str, str | int]] = []

        for row in item:
            tmp: dict[str, str | int] = {}
            for val in row:
                if isinstance(row[val], str):
                    tmp[val] = (
                        str(row[val])
                        .replace("'", "")
                        .replace('"', "")
                        .replace("\n", "")
                        .strip()
                    )
                else:
                    tmp[val] = row[val]
            clean.append(tmp)
        return clean
