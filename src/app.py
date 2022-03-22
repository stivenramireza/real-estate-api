import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from src.controllers.property_controller import PropertyController


class HTTPHandler(BaseHTTPRequestHandler, PropertyController):
    def do_GET(self) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        match self.path:
            case "/":
                self.wfile.write(bytes(self.root))
            case "/properties":
                status = None
                year = None
                city = None
                self.wfile.write(bytes(self.properties))
            case _:
                self.wfile.write(bytes(self.not_found_path))

    @property
    def root(self) -> object:
        return json.dumps(
            {"message": "Real Estate API is running successfully"}
        ).encode()

    @property
    def not_found_path(self) -> object:
        return json.dumps({"message": "Path not found"}).encode()
