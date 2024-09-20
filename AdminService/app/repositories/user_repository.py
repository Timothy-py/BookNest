
from app.core.database import user_collection

class UserRepository:
    async def add_user(user:dict):
        return await user_collection.insert_one(user)