
from sqlalchemy import Boolean, Column, Date, Integer, String, DateTime, func

from app.core.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    universal_id = Column(String(255), unique=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    category_universal_id = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)
    available_date = Column(Date, nullable=True)