from http.server import HTTPServer

from src.app import HTTPHandler
from src.utils.secrets import PORT, PYTHON_ENV
from src.utils.logger import logger


def main() -> None:
    app = HTTPServer(("0.0.0.0", int(PORT)), HTTPHandler)
    logger.info(f"Real Estate API is running at port {PORT} in {PYTHON_ENV} mode")
    app.serve_forever()


if __name__ == "__main__":
    main()
