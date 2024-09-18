from datetime import datetime
from fastapi.encoders import jsonable_encoder

from app.repositories.book_repository import BookRepository

class BookService:
    async def add_book(book):
        # convert pydantic model to dictionary
        book_dict = jsonable_encoder(book)
        
        # Add field
        book_dict["is_available"] = True
        book_dict["created_at"] = datetime.now()
        book_dict["updated_at"] = datetime.now()
        
        # Save to DB
        new_book = await BookRepository.add_book((book_dict))
        print(new_book)
        
        # Get inserted book
        result = await BookRepository.get_book_by_id(new_book.inserted_id)
        
        return result