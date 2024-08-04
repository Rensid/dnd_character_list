from sqlalchemy.orm import Session

from app.models.character_model import Character
from app.schemas import character_schema


def get_character(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()


def get_character_by_name(db: Session, character_name: str, user_id: int):
    return db.query(Character).filter(Character.name == character_name,
                                      Character.user_id == user_id).all()


def create_character(db: Session, character: character_schema.Character):
    db_character = Character()
