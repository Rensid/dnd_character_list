from pydantic import BaseModel


class CharacterBase(BaseModel):
    name: str
    lvl: int
    race: str
    spec_id: int
    strength: int
    multiclass: set[str] = set()
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    dexterity: int


class CharacterSchema(BaseModel):
    id: int
    user_id: int
