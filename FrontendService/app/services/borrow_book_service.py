

from datetime import datetime
import json
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


from app.core.database import database
from app.core.dependencies import RabbitMQClient
from app.models.borrow_book_model import BorrowBook
from app.schemas.borrow_book_schema import BorrowBookSchema
from app.services.book_service import BookService
from app.services.user_service import UserService


class BorrowBookService:
    async def borrow_book(book_id: int, data: BorrowBookSchema, producer: RabbitMQClient):
        try:
            current_date = datetime.now().strftime("%Y-%m-%d")
            current_date_obj = datetime.strptime(current_date, "%Y-%m-%d").date()
            # Get user
            data_dict = jsonable_encoder(data)
            user = await UserService.get_user_by_id(data_dict["user_id"])
            # Get book
            book = await BookService.get_book_by_id(book_id)
            
            # Check if book is available
            if book.is_available is False:
                raise HTTPException(status_code=400, detail="Book is not available")
            
            # Create borrow book
            async with database.get_session() as session:
                new_borrow_book = BorrowBook(borrower_universal_id=user.universal_id, book_universal_id=book.universal_id, return_date=data.return_date, borrowed_date=current_date_obj)
                session.add(new_borrow_book)
                await session.commit()
                await session.refresh(new_borrow_book)
                
            # Update book
            date_obj = datetime.strptime(data_dict["return_date"], "%Y-%m-%d").date()
            await BookService.update_book_availability(book_id, False, date_obj)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        else:
            # Publish borrow book
            date_string = date_obj.strftime("%Y-%m-%d")
            await producer.publish("borrow_book", json.dumps({"borrower_universal_id": user.universal_id, "book_universal_id": book.universal_id, "borrowed_date": current_date, "return_date": date_string, "returned": False}))
            return new_borrow_book