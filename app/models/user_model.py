from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Integer, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    hashed_password = Column(String)
    list_of_characters = relationship(
        "Character", backref="owner", cascade="all, delete"
    )
    is_active = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)


class EmailVerification(Base):
    __tablename__ = 'email_verification'

    uuid = Column(UUID(as_uuid=True), primary_key=True,
                  default=uuid4, unique=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    created = Column(DateTime(timezone=True), server_default=func.now())
    expiretion = Column(DateTime(timezone=True), server_default=func.now())
