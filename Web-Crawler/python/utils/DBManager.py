from __future__ import annotations
from datetime import datetime
import json
import mysql.connector


class DBManager:
    def __init__(self, path: str, auto_connect: bool = True) -> None:
        with open(path) as file:
            data = json.load(file)
            self.host = data["host"]
            self.database = data["database"]
            self.user = data["user"]
            self.password = data["password"]
            self.port = data["port"]
            self.table_name = ""

        if auto_connect:
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

    def insert(self, columns: list[str], items: str) -> None:
        try:
            pretty_columns = ", ".join(col for col in columns)
            self.cursor.execute(
                f"insert into {self.table_name} ({pretty_columns}) values({items})"
            )
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
