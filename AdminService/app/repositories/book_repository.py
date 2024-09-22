from datetime import date
from typing import Any
from bson import ObjectId

from app.core.database import book_collection

class BookRepository:
    async def add_book(book:dict) -> Any:
        return await book_collection.insert_one(book)

    async def get_book_by_id(book_id:str) -> dict:
        return await book_collection.find_one(filter={"_id": ObjectId(oid=book_id)})
    
    async def get_book_by_universal_id(universal_id:str) -> dict:
        return await book_collection.find_one({"universal_id": universal_id})

    async def delete_book_by_id(book_id:str):
        return await book_collection.delete_one(filter={"_id": ObjectId(oid=book_id)} )
    
    async def update_book_availability(universal_id:str, is_available:bool, available_date:date):
        return await book_collection.update_one({"universal_id": universal_id}, {"$set": {"is_available": is_available, "available_date": available_date}})
    
    async def get_unavailable_books(page:int, size:int):
        skip = (page - 1) * size
        query = {"is_available": False}
        
        books_cursor = book_collection.find(query).skip(skip).limit(size)
        books = await books_cursor.to_list(length=size)
        return books