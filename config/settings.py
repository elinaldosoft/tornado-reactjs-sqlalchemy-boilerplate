import os
from sqlalchemy import create_engine
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

# Path templates html
TEMPLATES = os.path.join(BASE_DIR, "templates")
# Files statics css, js, img
STATIC = os.path.join(BASE_DIR, "static")

PORT = config("PORT", default="8888", cast=int)
HOST = config("HOST", default="localhost")

ENGINE = create_engine(config("DATABASE_URL", cast=str), pool_size=10, max_overflow=20)

REDIS_HOST = config("REDIS_HOST", default="localhost")
REDIS_PORT = config("REDIS_PORT", default=6379, cast=int)

# https://www.tornadoweb.org/en/stable/template.html#tornado.template.BaseLoader
AUTOESCAPE = config("AUTOESCAPE", default=None)
