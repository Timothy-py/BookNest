from fastapi import APIRouter, status


from app.schemas.book_schema import BookResponse, AddBook
from app.services.book_service import BookService

book_router = APIRouter(prefix="/api/v1/books", tags=["Books"])


# ADD A BOOK
@book_router.post(path="/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def add_book(book: AddBook):
    return await BookService.add_book(book)