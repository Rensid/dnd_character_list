from fastapi import FastAPI
from app.db.base import metadata
from app.db.session import engine, SessionLocal
from fastapi.security import OAuth2PasswordBearer
from app.api.v1.endpoints.user_endpoint import users_router

metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users_router)
# app.include_router(characters_router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
