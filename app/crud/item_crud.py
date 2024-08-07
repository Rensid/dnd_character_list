from app.models.item_model import Item
from app.schemas.item_schema import ItemSchema, ItemBase
from sqlalchemy.orm import Session
from fastapi import HTTPException


def get_item(db: Session, item_id):
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db: Session, item: ItemBase):
    db_item = Item(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item: ItemSchema):

    # ? функция обновляет поля предмета.
    # ? сначала находит пользователя в базе. если он есть,
    # ? то из схемы исключает поле id чтобы не обновлять его.
    # ? после чего проходится циклом по всем полям обновленного словаря
    # ? и присваивает значения соответствующим полям

    db_item = db.query(Item).filter(Item.id == item.id).first()
    if db_item:
        update_item_data = item.dict(exclude={"id"})
        for key, value in update_item_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def delete_item(db: Session, item_id):
    db_item = db.query(Item.id == item_id).first()
    if db_item:
        db.delete()
        return db_item
    else:
        return None
