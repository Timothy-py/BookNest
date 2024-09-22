
from sqlalchemy import Column, Integer, String, DateTime, func

from app.core.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    universal_id = Column(String(255), unique=True, nullable=False)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())