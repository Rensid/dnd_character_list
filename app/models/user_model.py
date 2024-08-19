from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    list_of_characters = relationship(
        "Character", backref="owner", cascade="all, delete"
    )
    is_active = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)
