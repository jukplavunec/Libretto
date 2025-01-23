from __future__ import annotations
from sqlalchemy import Column, DateTime, Integer, Text, Boolean, func
from src.domain.models import User
from src.storages.db import Base


class UsersModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(Text, unique=True, nullable=False, index=True)
    username = Column(Text, unique=True, nullable=True, index=True)
    hashed_password = Column(Text, nullable=False)
    user_state = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified_email = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def to_orm(self, user: User) -> UsersModel:
        # TODO: make mapper class for all to_domain -> to_orm
        return UsersModel(
            email=user.email,
            username=user.name,
            user_state=user.user_state,
        )

    def to_domain(self) -> User:
        return User(
            name=self.username,
            email=self.email,
            user_state=self.user_state
        )

    def __repr__(self):
        return f"<User {self.email}>"

    def __str__(self):
        return f"<User {self.email}>"
    

