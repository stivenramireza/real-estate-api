import json

from src.services.property_service import PropertyService


class PropertyController:

    property_service = PropertyService()

    def properties(self, status: str, year: int, city: str) -> object:
        properties = self.property_service.get_properties(status, year, city)
        return json.dumps(properties).encode()

    def get_property_query_params(self, query_params) -> tuple[str, str, str]:
        return (
            query_params.get("status", [None])[0],
            query_params.get("year", [None])[0],
            query_params.get("city", [None])[0],
        )
