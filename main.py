from fastapi import FastAPI
from app.db.base import metadata, engine, SessionLocal
from fastapi.security import OAuth2PasswordBearer
from app.api.v1.endpoints.user import users_router

metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users_router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
