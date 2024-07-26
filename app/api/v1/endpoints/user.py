from fastapi import APIRouter
from sqlalchemy.orm import Session
users_router = APIRouter()


@users_router.get('/гusers')
async def get_users(db: Session, user_id: int):
    

@users_router.post("/users")
async def create_user():
    pass