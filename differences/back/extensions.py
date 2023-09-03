from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from argon2 import PasswordHasher
from flask_jwt_extended import JWTManager



db  = SQLAlchemy()

migrate = Migrate()


cors = CORS()

ph = PasswordHasher()

jwt = JWTManager()