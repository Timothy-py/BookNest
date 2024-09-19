from typing import Any
from bson import ObjectId

from app.core.database import book_collection

class BookRepository:
    async def add_book(book:dict) -> Any:
        return await book_collection.insert_one(book)

    async def get_book_by_id(book_id:str) -> dict:
        return await book_collection.find_one(filter={"_id": ObjectId(oid=book_id)})

    async def delete_book_by_id(book_id:str):
        return await book_collection.delete_one(filter={"_id": ObjectId(oid=book_id)} )