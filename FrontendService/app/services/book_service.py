

from app.core.database import get_session
from app.models.book_model import Book
from app.services.category_service import CategoryService


class BookService:
    async def add_book(data: dict):
        category = await CategoryService.get_category_by_title(data.get('category_title'))
        data['category_id'] = category.id
        # remove category_title from data
        del data['category_title']
        async with get_session() as session:
            new_book = Book(**data)
            session.add(new_book)
            await session.commit()
            await session.refresh(new_book)
        return new_book