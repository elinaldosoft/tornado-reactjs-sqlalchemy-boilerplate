import redis
from decouple import config
from config import settings


def connect():
    pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    return redis.Redis(connection_pool=pool)
