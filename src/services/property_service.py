from src.repositories.property_repository import PropertyRepository
from src.utils.enums import PropertyStatus
from src.utils.mapper import PropertyMapper


class PropertyService:

    property_repository = PropertyRepository()
    property_mapper = PropertyMapper()

    def get_properties(self, status: str, year: int, city: str) -> list[dict[str, any]]:
        self.validate_property_params(status, year, city)

        if status:
            status = self.property_mapper.map_property_status(status)

        properties = self.property_repository.get_properties(status, year, city)
        if not properties:
            return []
        return properties

    def validate_property_params(self, status: str, year: int, city: str) -> None:
        property_status = [status.name for status in PropertyStatus]
        if status and status not in property_status:
            raise Exception(
                "Invalid status. It must be one the following enums {}".format(
                    ", ".join(property_status)
                )
            )

        if year and not year.isnumeric():
            raise Exception("Invalid year. It must be a number")

        if city and not isinstance(city, str):
            raise Exception("Invalid city. It must be a string")
