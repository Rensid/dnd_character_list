from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.user_crud import clear_username, get_user_by_id, check_user_by_email_or_username, create_new_user, update_user, delete_user, update_user_password
from app.schemas.user_schema import UserSchema, UserPasswordSchema, UserBase
from app.db.session import get_db

users_router = APIRouter()


@users_router.get('/users/{user_id}', response_model=UserSchema)
def get_users(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@users_router.post("/users/", response_model=UserSchema)
def create_user(user: UserPasswordSchema,
                db: Session = Depends(get_db)):
    db_user = check_user_by_email_or_username(user, db)
    if db_user:
        raise HTTPException(
            status_code=400, detail="username or email already registered")
    else:
        db_user = create_new_user(db, user)
        return db_user


@users_router.put("/users/{user_id}/", response_model=UserSchema)
def user_update(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    return db_user


@users_router.put("/users/{user_id}", response_model=UserSchema)
def reset_password(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    db_user = update_user_password(db, user_id, user)
    return db_user


@users_router.delete("/users/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    return user


@users_router.delete("/users/{username}/")
def delete_user_by_username(username: str, db: Session = Depends(get_db)):
    user = clear_username(db, username)
    return user
