


from fastapi import APIRouter, Depends, status

from app.schemas.borrow_book_schema import BorrowBookSchema
from app.core.dependencies import RabbitMQClient, get_rabbitmq_client
from app.services.borrow_book_service import BorrowBookService


borrow_book_router = APIRouter(prefix="/api/v1/borrow_books", tags=["Borrow books"])


# Borrow Book
@borrow_book_router.post("/{book_id}", status_code=status.HTTP_201_CREATED)
async def borrow_book(book_id:int, data: BorrowBookSchema, producer:RabbitMQClient = Depends(get_rabbitmq_client)):
    return await BorrowBookService.borrow_book(book_id, data, producer)