from src.repositories.database_repository import db_connection, DatabaseRepository
from src.utils.queries import (
    PROPERTIES,
    STATUS_FILTER,
    YEAR_FILTER,
    CITY_FILTER,
)


class PropertyRepository:

    database_repository = DatabaseRepository()

    def get_properties(self, status: str, year: int, city: str) -> list[dict[str, any]]:
        properties_to_search = [PROPERTIES]

        if status or year or city:
            if status:
                properties_to_search.append(STATUS_FILTER.format(status))
            if year:
                properties_to_search.append(YEAR_FILTER.format(year))
            if city:
                properties_to_search.append(CITY_FILTER.format(city))
            properties_to_search = " AND ".join(properties_to_search)
        else:
            properties_to_search = PROPERTIES

        properties = self.database_repository.read_from_db(
            properties_to_search, db_connection
        )
        return properties
