from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, UUID4
from app.schemas.character_schema import CharacterSchema
from typing import Annotated


class UserBase(BaseModel):
    email: EmailStr
    username: Annotated[str, Field(max_length=50)]


class UserPasswordSchema(UserBase):
    hashed_password: str


class UserSchema(UserBase):
    id: Annotated[int, Field(gt=0)]
    characters: list[CharacterSchema] = []

    class Config:
        orm_mode = True
        from_attributes = True


class TokenData(BaseModel):
    id: int | None = None
    username: str | None = None


class Token(BaseModel):
    access: str
    refresh: str


class EmailVerification(BaseModel):
    uuid: UUID4
    user_id: int
    created: datetime
    expiretional: datetime
