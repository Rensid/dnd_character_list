from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.user import get_user, check_user_by_email_or_username, create_new_user, update_user, delete_user
from app.schemas.user_schema import UserSchema, UserPasswordSchema
from app.db.session import get_db

users_router = APIRouter()


@users_router.get('/users/{user_id}', response_model=UserSchema)
def get_users(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@users_router.post("/users/", response_model=UserSchema)
def create_user(user: UserPasswordSchema,
                db: Session = Depends(get_db)):
    db_user = check_user_by_email_or_username(db, user)
    if db_user:
        raise HTTPException(
            status_code=400, detail="username or email already registered")
    else:
        db_user = create_new_user(db, user)


@users_router.put("/users/", response_model=UserSchema)
def user_update(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
