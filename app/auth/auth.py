from typing import Annotated
from fastapi import Depends, HTTPException, status
from app.auth.jwt import verify_password
from app.crud.user_crud import check_user_by_username, get_user_by_id
from app.db.session import get_db
from app.models.user_model import User
from app.schemas.user_schema import TokenData, UserPasswordSchema, UserSchema
from settings import oauth2_scheme
from config import SECRET_KEY, ALGORITHM

import jwt
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session


def authenticate_user(db: Session, username: str, password: str) -> User:
    user = check_user_by_username(username, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def get_current_user(db: Annotated[Session, Depends(get_db)],
                     token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        type: str = payload.get('type')
        if type == 'refresh':
            
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(id=user_id)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_by_id(db=db, user_id=token_data.id)
    if user is None:
        raise credentials_exception
    return user

# def get_current_user(db: Annotated[Session, Depends(get_db)],
#                      token: Annotated[str, Depends(oauth2_scheme)]) -> UserSchema:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = check_user_by_username(db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user
