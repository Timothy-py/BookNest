

from sqlalchemy import Boolean, Column, Date, Integer, String
from app.core.database import Base


class BorrowBook(Base):
    __tablename__ = "borrow_book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    borrower_universal_id = Column(String, nullable=False)
    book_universal_id = Column(String, nullable=False)
    borrowed_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=False)
    returned = Column(Boolean, default=False)