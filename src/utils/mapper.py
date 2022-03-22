from src.utils.enums import PropertyStatus


class PropertyMapper:
    def map_property_status(self, status: str) -> str:
        property_status = dict(map(lambda s: (s.name, s.value), PropertyStatus))
        return property_status.get(status)
