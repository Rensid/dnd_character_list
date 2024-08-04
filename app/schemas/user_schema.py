from pydantic import BaseModel, Field, EmailStr
from app.schemas.character_schema import Character
from typing import Annotated


class UserBase(BaseModel):
    email: Annotated[EmailStr, Field(max_length=50)]
    username: Annotated[str, Field(max_length=50)]


class UserPasswordSchema(UserBase):
    password: str


class UserSchema(UserBase):
    id: Annotated[int, Field(gt=0)]
    characters: list[Character] = []

    class Config:
        orm_mode = True
