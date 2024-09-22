from bson import ObjectId


from app.core.database import category_collection


class CategoryRepository:
    async def create_category(category:dict):
        return await category_collection.insert_one(category)
    
    async def get_categories():
        return await category_collection.find().to_list(length=None)
    
    async def get_category_by_universal_id(category_universal_id:str):
        return await category_collection.find_one({"universal_id": category_universal_id})
