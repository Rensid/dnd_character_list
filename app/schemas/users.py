from pydantic import BaseModel
from app.schemas.character import Character


class User(BaseModel):
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    characters: list[Character]
