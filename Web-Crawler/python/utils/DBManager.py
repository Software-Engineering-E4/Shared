from datetime import datetime
import mysql.connector


class DBManager:
    def __init__(
        self, *, host: str, database: str, user: str, password: str, port: str
    ) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.table_name = ""

        self.connector = mysql.connector.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        self.cursor = self.connector.cursor()

    def set_table_name(self, table_name: str) -> None:
        self.table_name = table_name

    def insert(self, items: str) -> None:
        try:
            self.cursor.execute(f"insert into {self.table_name} values({items})")
        except Exception as ex:
            print(ex)

    @staticmethod
    def format_data(response: dict[str, str | int | datetime]) -> str:
        out = ""

        for key in response.keys():
            if isinstance(key, str):
                formatted = str(response[key]).replace("'", "").replace('"', "")
                out += f"'{formatted}', "
            elif isinstance(response[key], datetime):
                pass
            else:
                out += f"{response[key]}, "

        return out[:-2:]

    def close(self) -> None:
        self.connector.commit()
        self.connector.close()
