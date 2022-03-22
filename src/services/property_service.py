from src.repositories.property_repository import PropertyRepository


class PropertyService:

    property_repository = PropertyRepository()

    def get_properties(self, status: str, year: int, city: str) -> list[dict[str, any]]:
        return self.property_repository.get_properties(status, year, city)
