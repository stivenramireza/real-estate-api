import json
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler

from src.controllers.property_controller import PropertyController


class HTTPHandler(BaseHTTPRequestHandler, PropertyController):
    def do_GET(self) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        query_params = parse_qs(urlparse(self.path).query)
        if self.path == "/":
            self.wfile.write(bytes(self.root))
        elif self.path.startswith("/properties"):
            status, year, city = self.get_property_query_params(query_params)
            self.wfile.write(bytes(self.properties(status, year, city)))
        else:
            self.wfile.write(bytes(self.not_found_path))

    @property
    def root(self) -> object:
        return json.dumps(
            {"message": "Real Estate API is running successfully"}
        ).encode()

    @property
    def not_found_path(self) -> object:
        return json.dumps({"message": "Path not found"}).encode()
