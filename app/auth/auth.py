from typing import Annotated
from fastapi import Depends, HTTPException, status
from app.auth.jwt import get_new_tokens, verify_password
from app.crud.user_crud import check_user_by_username, get_user_by_id
from app.db.session import get_db
from app.schemas.user_schema import TokenData
from settings import oauth2_scheme
from config import SECRET_KEY

import jwt
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session


def authenticate_user(db: Session, username: str, password: str):
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
        user_id: str = payload.get("sub")
        type: str = payload.get('type')
        if user_id is None or type is None:
            raise credentials_exception
        token_data = TokenData(id=user_id)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_by_id(db=db, user_id=token_data.id)
    if user is None:
        raise credentials_exception
    if type == "refresh":
        tokens = get_new_tokens(user)
        return {"user": user, "token": tokens}
    elif type == "access":
        return user
