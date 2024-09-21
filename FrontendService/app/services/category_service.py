

from sqlalchemy.future import select
from app.core.database import get_session
from app.models.category_model import Category

class CategoryService:
    async def create_category(data:dict):
        async with get_session() as session:
            new_category = Category(**data)
            session.add(new_category)
            await session.commit()
            await session.refresh(new_category)
        return new_category
    
    async def get_category_by_title(title: str):
        async with get_session() as session:
            result = await session.execute(select(Category).filter(Category.title == title))
            category = result.scalars().first()
            return category
        