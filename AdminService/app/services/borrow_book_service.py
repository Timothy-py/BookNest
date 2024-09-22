


from app.repositories.book_repository import BookRepository
from app.repositories.borrow_book_repository import BorrowBookRepository
from app.repositories.user_repository import UserRepository


class BorrowBookService:
    async def borrow_book(data):
        # UPdate book
        await BookRepository.update_book_availability(data["book_universal_id"], False, data["return_date"])
        
        # Get book
        book = await BookRepository.get_book_by_universal_id(data["book_universal_id"])
        
        # Pick title, author, publisher from book
        book_data = {
            "title": book["title"],
            "author": book["author"],
            "publisher": book["publisher"],
            "category": book["category"],
            "universal_id": book["universal_id"]
        }
        
        # Add book_data to data
        data["book"] = book_data
        
        result = await BorrowBookRepository.borrow_book(data)
        
        # updte user with borrowed_book
        await UserRepository.update_borrowed_book(data["borrower_universal_id"], result.inserted_id)