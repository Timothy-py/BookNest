

from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.core.dependencies import RabbitMQClient
from app.repositories.category_repository import CategoryRepository
from app.schemas.category_schema import CategorySchema


class CategoryService:
    async def create_category(data:CategorySchema, producer:RabbitMQClient):
        try:
            category_dict = jsonable_encoder(obj=data)
        
            new_catgory = await CategoryRepository.create_category(category_dict)
            
            result = await CategoryRepository.get_cagegory_by_id(new_catgory.inserted_id)
        except DuplicateKeyError:
            raise HTTPException(
                status_code=409, detail="Category already exists"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(object=e))
        else:
            # Publish to Frontend service
            await producer.publish("create_category", data.model_dump_json())
            return result
    
    async def get_categories():# -> list:
        categories = await CategoryRepository.get_categories()
        return categories