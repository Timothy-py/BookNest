from datetime import datetime
import json
from unicodedata import category
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.rabbitmq.rabbitmq_client import RabbitMQClient
from app.repositories.book_repository import BookRepository
from app.repositories.category_repository import CategoryRepository
from app.schemas.category_schema import CategorySchema

class BookService:
    async def add_book(data, producer:RabbitMQClient):
        try:
            # convert pydantic model to dictionary
            book_dict = jsonable_encoder(data)
            
            # Add field
            book_dict["is_available"] = True
            book_dict["created_at"] = datetime.now()
            book_dict["updated_at"] = datetime.now()
            
            # Get category
            document = await CategoryRepository.get_cagegory_by_id(book_dict["category_id"])
            if document is None:
                raise HTTPException(status_code=404, detail="Category not found")
            
            # Save to DB
            new_book = await BookRepository.add_book((book_dict))
            
            # Get inserted book
            result = await BookRepository.get_book_by_id(new_book.inserted_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(object=e))
        else:
            category = CategorySchema(**document)
            dict_cat = (category.dict())
            title = (dict_cat["title"])
            # Publish new book to Frontend service
            send_book = {
                "title": book_dict["title"],
                "description": book_dict["description"],
                "author": book_dict["author"],
                "publisher": book_dict["publisher"],
                "category_title": title,
                "quantity": book_dict["quantity"],
            }
            await producer.publish("add_book", json.dumps(send_book))
            return result
    
    # DELETE A BOOK
    async def delete_book(book_id):
        await BookRepository.delete_book_by_id(book_id)
        return