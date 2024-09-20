
from app.core.database import user_collection

class UserRepository:
    async def add_user(user:dict):
        return await user_collection.insert_one(user)
    
    async def get_users(skip:int, size:int):
        return await user_collection.find().skip(skip).limit(size).to_list(length=size)