from __future__ import annotations
from datetime import datetime
import json
import mysql.connector


class DBManager:
    def __init__(self, path: str) -> None:
        with open(path) as file:
            data = json.load(file)
            self.host = data["host"]
            self.database = data["database"]
            self.user = data["user"]
            self.password = data["password"]
            self.port = data["port"]
            self.table_name = ""

        self.connector = mysql.connector.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        self.cursor = self.connector.cursor()

    def __enter__(self) -> DBManager:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.connector.commit()
        self.connector.close()

    def set_table_name(self, table_name: str) -> None:
        self.table_name = table_name

    def insert(self, items: str) -> None:
        try:
            self.cursor.execute(f"insert into {self.table_name} values({items})")
        except mysql.connector.errors.IntegrityError as err:
            print(err)

    def execute(self, statement: str) -> None:
        try:
            self.cursor.execute(statement)
        except Exception as ex:
            print(ex)

    @staticmethod
    def format_data(response: dict[str, str | int | datetime]) -> str:
        out = ""

        for key in response.keys():
            if isinstance(response[key], str):
                formatted = str(response[key]).replace("'", "").replace('"', "")
                out += f"'{formatted}', "
            else:
                out += f"{response[key]}, "

        return out[:-2:]
