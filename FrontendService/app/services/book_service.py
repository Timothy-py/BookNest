
from datetime import date
from fastapi import HTTPException
from sqlalchemy.future import select


from app.core.database import database
from app.models.book_model import Book


db_session = database.get_session()
class BookService:
    async def add_book(data: dict):
        async with db_session as session:
            new_book = Book(**data)
            session.add(new_book)
            await session.commit()
            await session.refresh(new_book)
        return new_book
    
    async def list_books(page:int, size:int):
        skip = (page - 1) * size
        async with db_session as session:
            result = await session.execute(select(Book).offset(skip).limit(size))
            books = result.scalars().all()
        return {
            "books": books,
            "page": page,
            "size": size,
        }
        
    async def get_book_by_id(id: int):
        async with db_session as session:
            result = await session.execute(select(Book).filter(Book.id == id))
            book = result.scalars().first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    
    async def delete_book(book_universal_id: str):
        async with db_session as session:
            result = await session.execute(select(Book).filter(Book.universal_id == book_universal_id))
            book = result.scalars().first()
            if book is not None:
                await session.delete(book)
                await session.commit()

    async def update_book_availability(id:int, is_available: bool, available_date: date=None):
        async with db_session as session:
            result = await session.execute(select(Book).filter(Book.id == id))
            book = result.scalars().first()
            if book is not None:
                book.is_available = is_available
                book.available_date = available_date
                await session.commit()
                
    async def filter_books(publisher:str, category:str, page:int, size:int):
        async with db_session as session:
            offset = (page - 1) * size
            query = select(Book)
            
            if publisher:
                query = query.filter(Book.publisher == publisher)
            if category:
                query = query.filter(Book.category == category)
            
            result = await session.execute(query.offset(offset).limit(size))
            books = result.scalars().all()
            
            return {
            "books": books,
            "page": page,
            "size": size,
        }