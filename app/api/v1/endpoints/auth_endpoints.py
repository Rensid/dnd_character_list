from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.auth import authenticate_user, get_current_user
from app.auth.jwt import get_new_tokens
from app.db.session import get_db
from app.crud.user_crud import create_new_user
from app.models.user_model import User
from app.schemas.user_schema import Token, UserPasswordSchema, UserSchema

ACCESS_TOKEN_EXPIRE_MINUTES = 30

auth_router = APIRouter()


@auth_router.post('/login/')
def login_for_accees_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                           db: Session = Depends(get_db)) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    tokens = get_new_tokens(user)
    return Token(**tokens)


@auth_router.post('/registration')
async def register_new_user(user_data: UserPasswordSchema,
                            db: Session = Depends(get_db)):
    user = create_new_user(db, user_data)
    tokens = get_new_tokens(user)
    return tokens


@auth_router.get("/users/me/")
def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user
