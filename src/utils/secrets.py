import os

from dotenv import load_dotenv

from src.utils.logger import logger


PYTHON_ENV = os.environ.get("PYTHON_ENV")
if PYTHON_ENV == "production":
    dotenv_path = ".env"
    logger.info("Using production environment variables")
else:
    dotenv_path = ".env.dev"
    logger.info("Using development environment variables")

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception("env files do not exist")

load_dotenv(dotenv_path)


PORT = os.environ.get("PORT")
PYTHON_ENV = os.environ.get("PYTHON_ENV")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_SCHEMA = os.environ.get("DB_SCHEMA")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
