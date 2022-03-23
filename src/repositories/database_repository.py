from src.utils.secrets import DB_HOST, DB_PORT, DB_SCHEMA, DB_USER, DB_PASSWORD
from src.config.database import MySQLConnection


class DatabaseRepository:
    def read_from_db(self, sql: str, connection: object) -> list[dict[str, any]]:
        cursor = connection.cursor()
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        records = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return records


db_connection = MySQLConnection.get_instance(
    credentials={
        "DB_HOST": DB_HOST,
        "DB_PORT": DB_PORT,
        "DB_SCHEMA": DB_SCHEMA,
        "DB_USER": DB_USER,
        "DB_PASSWORD": DB_PASSWORD,
    }
)
