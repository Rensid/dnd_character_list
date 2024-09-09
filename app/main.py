from fastapi import FastAPI
from app.db.base import metadata
from app.db.session import engine
from app.api.v1.endpoints.user_endpoint import users_router
from app.api.v1.endpoints.auth_endpoints import auth_router
from starlette.middleware.sessions import SessionMiddleware
from config import SECRET_KEY

metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.include_router(users_router)
app.include_router(auth_router)

# app.include_router(characters_router)
