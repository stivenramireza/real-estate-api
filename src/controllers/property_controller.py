import json


class PropertyController:
    @property
    def properties(self) -> object:
        return json.dumps([]).encode()
