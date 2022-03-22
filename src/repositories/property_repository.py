from src.repositories.database_repository import db_connection, DatabaseRepository
from src.utils.queries import PROPERTIES, FILTERED_PROPERTIES


class PropertyRepository:

    database_repository = DatabaseRepository()

    def get_properties(self, status: str, year: int, city: str) -> list[dict[str, any]]:
        # properties = PROPERTIES + FILTERED_PROPERTIES if status or year or city else PROPERTIES
        properties = self.database_repository.read_from_db(PROPERTIES, db_connection)
        return properties
