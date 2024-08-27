from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.auth.jwt import get_password_hash
from app.models.user_model import User
from app.schemas.user_schema import UserSchema, UserPasswordSchema
from app.auth.verify import send_code_to_email, generate_secret_code
from settings import redis_verify_client


def check_user_by_email_or_username(user: UserPasswordSchema, db: Session) -> User:
    return db.query(User).filter(or_(User.email == user.email,
                                 User.username == user.username)).first()


def check_user_by_email(email: str, db: Session) -> User:
    return db.query(User).filter(User.email == email).first()


def check_user_by_username(username: str, db: Session) -> User:
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def create_new_user(db: Session, user: UserPasswordSchema) -> User:
    if check_user_by_email_or_username(user, db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="username or email already registered"
        )
    else:
        db_user = User(
            email=user.email,
            username=user.username,
            hashed_password=get_password_hash(user.hashed_password)
        )
    code = generate_secret_code()
    send_code_to_email.delay(user.email, code)
    redis_verify_client.setex(user.username, 300, code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id, updated_user: UserSchema):

    # ! Обновление пользователя
    # * Проверяет сначала заняты ли обновленные логин или почта,
    # * после чего ищет пользователя по id и если такой есть, то обновляет данные.

    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = updated_user.username
        db_user.list_of_characters = updated_user.characters
        db_user.email = updated_user.email
        db.commit()
        db.refresh(db_user)
    return db_user


def update_user_password(db: Session, user_id, updated_user: UserPasswordSchema):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db_user.hashed_password = updated_user.hashed_password
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def clear_username(db: Session, username):
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def create_verification_link():
    pass


def send_verification_email():
    pass
