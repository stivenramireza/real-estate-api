from src.repositories.database_repository import DatabaseRepository
from src.utils.queries import PROPERTIES


class PropertyRepository:

    database_repository = DatabaseRepository()

    def get_properties(self) -> list[dict[str, any]]:
        return self.database_repository.read_from_db(PROPERTIES)
