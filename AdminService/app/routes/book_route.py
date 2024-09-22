from fastapi import APIRouter, Depends, status


from app.core.dependencies import get_rabbitmq_client, RabbitMQClient
from app.schemas.book_schema import BookResponse, AddBook
from app.services.book_service import BookService

book_router = APIRouter(prefix="/api/v1/books", tags=["Books"])


# ADD A BOOK
@book_router.post(path="/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def add_book(book: AddBook, producer:RabbitMQClient = Depends(get_rabbitmq_client)):
    return await BookService.add_book(book, producer)

# DELETE A BOOK
@book_router.delete(path="/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str, producer:RabbitMQClient = Depends(get_rabbitmq_client)):
    return await BookService.delete_book(book_id, producer)

# GET UNAVAILABLE BOOKS
@book_router.get(path="/unavailable_books", response_model=list[BookResponse], status_code=status.HTTP_200_OK)
async def get_unavailable_books(page: int = 1, size: int = 10):
    return await BookService.get_unavailable_books(page, size)