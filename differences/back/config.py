from datetime import timedelta
import os

from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.environ.get("SECRET_KEY")


FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT", 8000)
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", False)
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes = 20)