from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserSchema, UserPasswordSchema

'''
    TODO:  после того как сделаю авторизацию 
    через google и apple надо переделать функции, 
    тк поля будут не совпадать
'''


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def check_user_by_email_or_username(db: Session, username: str, email: str):
    user = db.query(User).filter(User.email == email,
                                 User.username == username).first()
    if user:
        return user
    else:
        return None


def create_new_user(db: Session, user: UserPasswordSchema):
    fake_hashed_password = user.password + 'notreallyhashed'
    db_user = User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ! Обновление пользователя
# * Проверяет сначала заняты ли обновленные логин или почта,
# * после чего ищет пользователя по id и если такой есть, то обновляет данные.


def update_user(db: Session, user_id, updated_user: UserSchema):

    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = updated_user.username
        db_user.list_of_characters = updated_user.list_of_characters
        db_user.email = updated_user.email
        db.commit()
        db.refresh(db_user)
    return db_user


# def update_user_password(db: Session, user_id, updated_user: UserPasswordSchema):


def delete_user(db: Session, user_id):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
