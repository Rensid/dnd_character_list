from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import redis
from celery import Celery
import os
from config import REDIS_HOST

celery_app = Celery(__name__, broker=f'redis://{REDIS_HOST}:6379/0',
                    backend=f'redis://{REDIS_HOST}:6379/0', include=['app.auth.verify'])

redis_client = redis.StrictRedis(
    host=f'{REDIS_HOST}', port=6379, db=0, decode_responses=True)

redis_verify_client = redis.StrictRedis(host=f'{REDIS_HOST}', port=6379, db=1,
                                        decode_responses=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
