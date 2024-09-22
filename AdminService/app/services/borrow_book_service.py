


from app.repositories.book_repository import BookRepository
from app.repositories.borrow_book_repository import BorrowBookRepository


class BorrowBookService:
    async def borrow_book(data):
        # UPdate book
        await BookRepository.update_book_availability(data["book_universal_id"], False, data["return_date"])
        await BorrowBookRepository.borrow_book(data)