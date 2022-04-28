import mysql.connector

class DBManager:
    def __init__(
        self, *, host: str, database: str, user: str, password: str, port: str = "5432"
    ) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

        self.table_name = ""
        self.keys: list[str] = []

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

    def set_keys(self, keys: list[str]) -> None:
        self.keys = keys

    def execute(self, statement: str) -> None:
        try:
            self.cursor.execute(statement)
        except Exception as ex:
            print(ex)

    def close(self) -> None:
        self.connector.commit()
        self.connector.close()

    def reset(self) -> None:
        self.cursor.execute(f"truncate table {self.table_name}")
        self.connector.commit()
