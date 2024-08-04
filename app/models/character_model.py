from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.user_model import User
from app.models.associations import characters_items


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lvl = Column(Integer)
    race = Column(String)
    spec_id = Column(Integer)
    strength = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)
    dexterity = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    items = relationship('Item', secondary=characters_items,
                         back_populates='character_who_equip')
