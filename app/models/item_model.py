from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.associations import characters_items
from app.db.base import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    bonus_strength = Column(Integer)
    bonus_constitution = Column(Integer)
    bonus_intelligence = Column(Integer)
    bonus_wisdom = Column(Integer)
    bonus_charisma = Column(Integer)
    bonus_dexterity = Column(Integer)
    is_equipped = Column(Boolean)
    character_who_equip = relationship(
        'Character', secondary=characters_items, back_populates='items')
