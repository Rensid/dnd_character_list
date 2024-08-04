from pydantic import BaseModel


class Character(BaseModel):
    id: int
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
