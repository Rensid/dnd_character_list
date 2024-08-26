from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import redis
import smtplib
from email.message import EmailMessage

redis_client = redis.StrictRedis(
    host='localhost', port=6379, db=0, decode_responses=True)

redis_verify_client = redis.StrictRedis(host='localhost', port=6379, db=1,
                                        decode_responses=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
