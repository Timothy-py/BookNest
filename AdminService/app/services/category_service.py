

from fastapi.encoders import jsonable_encoder

from app.repositories.category_repository import CategoryRepository


class CategoryService:
    async def create_category(category):
        category_dict = jsonable_encoder(category)
        
        new_catgory = await CategoryRepository.create_category(category_dict)
        
        result = await CategoryRepository.get_cagegory_by_id(new_catgory.inserted_id)
        return result
    
    async def get_categories():
        categories = await CategoryRepository.get_categories()
        return categories