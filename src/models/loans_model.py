from sqlalchemy import Column, Integer, Date, DateTime, func
from src.storages.db import Base


class LoansModel(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    book_id = Column(Integer)
    loan_date = Column(Date)
    return_date = Column(Date)
    created_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
