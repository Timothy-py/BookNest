
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func

from app.core.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    category_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)