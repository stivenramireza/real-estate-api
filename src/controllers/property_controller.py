import json

from src.services.property_service import PropertyService


class PropertyController:

    property_service = PropertyService()

    @property
    def properties(self, status: str = None, year: int = None, city: str = None) -> object:
        properties = self.property_service.get_properties(status, year, city)
        return json.dumps(properties).encode()
