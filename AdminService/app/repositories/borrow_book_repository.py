

from app.core.database import borrow_book_collection

class BorrowBookRepository:
    async def borrow_book(data: dict):
        return await borrow_book_collection.insert_one(data)