from fastapi import APIRouter, status


from app.schemas.book_schema import BookResponse, AddBook
from app.services.book_service import BookService

book_router = APIRouter(prefix="/api/v1/books", tags=["Books"])


# ADD A BOOK
@book_router.post(path="/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def add_book(book: AddBook):
    return await BookService.add_book(book)

# DELETE A BOOK
@book_router.delete(path="/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str):
    return await BookService.delete_book(book_id)