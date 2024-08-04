from pydantic import BaseModel


class Item(BaseModel):
    id: int
    description: str
    bonus_strength: int | None = None
    bonus_constitution: int | None = None
    bonus_intelligence: int | None = None
    bonus_wisdom: int | None = None
    bonus_charisma: int | None = None
    bonus_dexterity: int | None = None
    is_equipped: bool
