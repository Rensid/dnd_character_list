from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import Base

characters_items = Table('characters_items', Base.metadata,
                         Column('character_id', Integer, ForeignKey(
                             'characters.id', ondelete='CASCADE'), primary_key=True),
                         Column('item_id', Integer, ForeignKey(
                             'items.id', ondelete='CASCADE'), primary_key=True)
                         )
