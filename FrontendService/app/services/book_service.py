
from fastapi import HTTPException
from sqlalchemy.future import select


from app.core.database import get_session
from app.models.book_model import Book
from app.services.category_service import CategoryService


class BookService:
    async def add_book(data: dict):
        async with get_session() as session:
            new_book = Book(**data)
            session.add(new_book)
            await session.commit()
            await session.refresh(new_book)
        return new_book
    
    async def list_books(page:int, size:int):
        skip = (page - 1) * size
        async with get_session() as session:
            result = await session.execute(select(Book).offset(skip).limit(size))
            books = result.scalars().all()
        return {
            "books": books,
            "page": page,
            "size": size,
        }
        
    async def get_book_by_id(id: int):
        async with get_session() as session:
            result = await session.execute(select(Book).filter(Book.id == id))
            book = result.scalars().first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    
    async def delete_book(book_universal_id: str):
        async with get_session() as session:
            result = await session.execute(select(Book).filter(Book.universal_id == book_universal_id))
            book = result.scalars().first()
            if book is not None:
                await session.delete(book)
                await session.commit()
