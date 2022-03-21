import json

from src.services.property_service import PropertyService


class PropertyController:

    property_service = PropertyService()

    @property
    def properties(self) -> object:
        properties = self.property_service.get_properties()
        return json.dumps(properties).encode()
