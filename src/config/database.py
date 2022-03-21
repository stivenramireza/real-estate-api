from mysql.connector import connect, Error

from src.utils.secrets import DB_HOST, DB_PORT, DB_SCHEMA, DB_USER, DB_PASSWORD
from src.utils.logger import logger


class MySQLConnection:

    _instance = None

    def __init__(
        self, host: str, port: str, schema: str, user: str, password: str
    ) -> None:
        self.host = host
        self.port = port
        self.schema = schema
        self.user = user
        self.password = password
        self.connect()

    def connect(self) -> None:
        if MySQLConnection._instance is None:
            try:
                MySQLConnection._instance = connect(
                    host=self.host,
                    user=self.user,
                    passwd=self.password,
                    database=self.schema,
                    port=self.port,
                )
                logger.info("Connected to MySQL database successfully")
            except Error as e:
                logger.error(f"Error to connect to MySQL database: {e}")
        else:
            raise Exception("You cannot create another MySQL connection")

    @staticmethod
    def get_instance(credentials: dict) -> object:
        if not MySQLConnection._instance:
            MySQLConnection(
                host=credentials.get("DB_HOST"),
                port=credentials.get("DB_PORT"),
                schema=credentials.get("DB_SCHEMA"),
                user=credentials.get("DB_USER"),
                password=credentials.get("DB_PASSWORD"),
            )
        return MySQLConnection._instance

    @staticmethod
    def close_instance() -> None:
        if MySQLConnection._instance.is_connected():
            MySQLConnection._instance.close()
            logger.info("MySQL connection has been closed")


conn_mysql = MySQLConnection.get_instance(
    credentials={
        "DB_HOST": DB_HOST,
        "DB_PORT": DB_PORT,
        "DB_SCHEMA": DB_SCHEMA,
        "DB_USER": DB_USER,
        "DB_PASSWORD": DB_PASSWORD,
    }
)


def read_from_db(sql: str, conn: object) -> list[dict[str, any]]:
    cursor = conn.cursor()
    cursor.execute(sql)
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
