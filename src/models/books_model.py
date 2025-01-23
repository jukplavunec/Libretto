from sqlalchemy import Column, DateTime, Integer, Text, func
from src.storages.db import Base


class BooksModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, index=True)
    author = Column(Text, index=True)
    genre = Column(Text)
    year = Column(Text)
    state = Column(Text)
    created_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, genre={self.genre}, year={self.year}, state={self.state})"

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, genre={self.genre}, year={self.year}, state={self.state})"
