from datetime import datetime
import json
from unicodedata import category
import uuid
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.rabbitmq.rabbitmq_client import RabbitMQClient
from app.repositories.book_repository import BookRepository
from app.repositories.category_repository import CategoryRepository
from app.schemas.category_schema import CategorySchema

class BookService:
    async def add_book(data, producer:RabbitMQClient):
        try:
            universal_id = str(uuid.uuid4())
            # convert pydantic model to dictionary
            book_dict = jsonable_encoder(data)
            
            # Add field
            book_dict["is_available"] = True
            book_dict["created_at"] = datetime.now()
            book_dict["updated_at"] = datetime.now()
            book_dict["universal_id"] = universal_id
            
            # Get category
            document = await CategoryRepository.get_category_by_universal_id(book_dict["category_universal_id"])
            if document is None:
                raise HTTPException(status_code=404, detail="Category not found")
            
            # Save to DB
            new_book = await BookRepository.add_book((book_dict))
            
            # Get inserted book
            result = await BookRepository.get_book_by_id(new_book.inserted_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(object=e))
        else:
            # Update the data to include the universal_id
            data_with_universal_id = data.model_dump()
            data_with_universal_id["universal_id"] = universal_id
            # Publish new book to Frontend service
            await producer.publish("add_book", json.dumps(data_with_universal_id))
            return result
    
    # DELETE A BOOK
    async def delete_book(book_id, producer:RabbitMQClient):
        # Get book by id
        book = await BookRepository.get_book_by_id(book_id)
        print(book)
        if book is not None:
            message = json.dumps({"book_universal_id": book["universal_id"]}) 
            await producer.publish("delete_book", message)
            await BookRepository.delete_book_by_id(book_id)
        return