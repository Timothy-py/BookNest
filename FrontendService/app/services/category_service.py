

from app.core.database import get_session
from app.models.category_model import Category
# from app.repositories.category_repository import CategoryRepository

class CategoryService:
    async def create_category(data:dict):
        async with get_session() as session:
            new_category = Category(**data)
            session.add(new_category)
            await session.commit()
            await session.refresh(new_category)
        return new_category
        