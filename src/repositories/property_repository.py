from src.repositories.database_repository import db_connection, DatabaseRepository
from src.utils.queries import PROPERTIES, PROPERTIES_WITH_FILTERS


class PropertyRepository:

    database_repository = DatabaseRepository()

    def get_properties(self, status: str, year: int, city: str) -> list[dict[str, any]]:
        if status or year or city:
            properties_to_search = f"{PROPERTIES}{PROPERTIES_WITH_FILTERS}"
            values = (status, year, city)
        else:
            properties_to_search = PROPERTIES
            values = ()

        properties = self.database_repository.read_from_db(
            properties_to_search, values, db_connection
        )
        return properties
