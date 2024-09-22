
from app.core.database import user_collection

class UserRepository:
    async def add_user(user:dict):
        return await user_collection.insert_one(user)
    
    async def get_users(skip:int, size:int):
        return await user_collection.find().skip(skip).limit(size).to_list(length=size)
    
    async def update_borrowed_book(universal_id:str, borrowed_book_id:str):
        return await user_collection.update_one({"universal_id":universal_id}, {"$push": {"borrowed_books": borrowed_book_id}})
    
    async def get_users_with_borrowed_books(skip:int, size:int):
        pipeline = [
            {
                "$lookup": {
                    "from": "borrow_book_collection", # Collection to join with
                    "localField": "borrowed_books", # Field in users collection
                    "foreignField": "_id", # Field in borrowed_books collection
                    "as": "borrowed_books" # Output array with borrowed books
                }
            },
            {
                '$skip': skip,
            },
            {
                '$limit': size
            }
        ]
        
        users = await user_collection.aggregate(pipeline).to_list(length=None)
        return users