from sqlalchemy.orm import Session
import json
from app.models.character_model import Character
from app.schemas.character_schema import CharacterSchema, CharacterBase


def get_character(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()


def get_character_by_name(db: Session, character_name: str, user_id: int):
    return db.query(Character).filter(Character.name == character_name,
                                      Character.user_id == user_id).all()


def create_character(db: Session, character: CharacterBase):
    db_character = Character(
        **character
    )
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


def update_character(db: Session, character: CharacterSchema):

    # ? функция обновляет поля персонажа.
    # ? сначала находит пользователя в базе. если он есть,
    # ? то из схемы исключает поле id чтобы не обновлять его.
    # ? после чего проходится циклом по всем полям обновленного словаря
    # ? и присваивает значения соответствующим полям

    db_character = db.query(Character).filter(
        Character.user_id == character.user_id,
        Character.id == character.id).first()
    if db_character:
        character_data = character.dict(exclude={"id", "user_id"})
        if "multiclass" in character_data:
            character_data["multiclass"] = json.dumps(
                list(character_data["multiclass"]))
        for key, value in character_data.items():
            setattr(db_character, key, value)
        db.commit()
        db.refresh(db_character)
        return db_character
    else:
        return None


def delete_character(db: Session, character: CharacterSchema):
    db_character = db.query(Character).filter(
        Character.id == character.id, Character.user_id == character.user_id).first()
    if db_character:
        db.delete(db_character)
        return db_character
